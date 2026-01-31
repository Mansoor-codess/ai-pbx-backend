from fastapi import FastAPI, Depends, WebSocket, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db, engine
from app.models import Base, Call, CallState
from app.schemas import Packet
from app.ai_service import mock_ai_service
from app.retry import retry_with_backoff
from app.websocket_manager import ConnectionManager

app = FastAPI()
manager = ConnectionManager()


# -------------------- STARTUP --------------------

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# -------------------- INGEST API --------------------

@app.post("/v1/call/stream/{call_id}", status_code=202)
async def ingest_packet(
    call_id: str,
    packet: Packet,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):

    # Lock row to avoid race condition
    result = await db.execute(
        select(Call).where(Call.call_id == call_id).with_for_update()
    )

    call = result.scalar_one_or_none()

    # Safe creation (handles double insert race condition)
    if not call:
        try:
            call = Call(call_id=call_id)
            db.add(call)
            await db.commit()
            await db.refresh(call)

        except Exception:
            # Another request created it at same time
            await db.rollback()

            result = await db.execute(
                select(Call).where(Call.call_id == call_id).with_for_update()
            )

            call = result.scalar_one()

    # Sequence validation
    if packet.sequence != call.last_sequence + 1:
        print("⚠ Packet missing!")

    call.last_sequence = packet.sequence

    # Trigger AI processing after last packet
    if packet.sequence == 5:
        background_tasks.add_task(process_ai, call_id)

    await db.commit()

    return {"message": "Packet accepted"}


# -------------------- WEBSOCKET --------------------

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)


# -------------------- BACKGROUND AI TASK --------------------

async def process_ai(call_id: str):

    # Create NEW DB session for background task
    async for db in get_db():

        result = await db.execute(
            select(Call).where(Call.call_id == call_id)
        )

        call = result.scalar_one_or_none()

        if not call:
            return

        call.state = CallState.PROCESSING_AI
        await db.commit()

        try:
            text = await retry_with_backoff(
                lambda: mock_ai_service("sample audio")
            )

            call.transcription = text
            call.state = CallState.ARCHIVED

            await manager.broadcast(
                f"Call {call_id} processed successfully"
            )

        except Exception as e:
            print("AI Processing Failed:", e)
            call.state = CallState.FAILED

        await db.commit()

        break
