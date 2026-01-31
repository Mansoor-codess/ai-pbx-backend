import pytest
import asyncio
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_simultaneous_packets():

    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:

        payload1 = {
            "sequence": 1,
            "data": "packet one",
            "timestamp": 1.1
        }

        payload2 = {
            "sequence": 2,
            "data": "packet two",
            "timestamp": 1.2
        }

        response1, response2 = await asyncio.gather(
            client.post("/v1/call/stream/testcall", json=payload1),
            client.post("/v1/call/stream/testcall", json=payload2)
        )

        assert response1.status_code == 202
        assert response2.status_code == 202
