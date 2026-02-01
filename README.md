🚀 AI-PBX Backend System — FastAPI Voice & AI Microservice

A high-performance asynchronous backend system designed to simulate an enterprise-grade PBX (Private Branch Exchange) AI routing service. This project demonstrates scalable API ingestion, fault-tolerant AI orchestration, database concurrency handling, and real-time WebSocket communication.

This system is built as part of a technical evaluation for the FastAPI Backend Intern (Voice & AI Team) role.

📌 Problem Statement

Modern PBX systems handle thousands of concurrent calls. When human agents are unavailable, calls must be routed to AI voice bots. These AI services are often slow and unreliable.

This project solves the following challenges:

High-throughput packet ingestion

Maintaining packet order

Handling flaky AI APIs

Background processing

Concurrency & race condition handling

Real-time supervisor updates

🎯 Project Goals

✔ Accept streaming audio metadata asynchronously
✔ Process AI transcription without blocking API
✔ Maintain call lifecycle state machine
✔ Handle concurrent database writes safely
✔ Recover from AI failures automatically
✔ Broadcast live system updates

⚙ Core Features
🚀 Asynchronous API Architecture

Non-blocking FastAPI endpoints

Sub-50ms response target

Async SQLAlchemy engine

📦 Packet Streaming Validation

Accepts streaming packet metadata

Sequence validation logic

Missing packet detection with logging

No request blocking

🔁 Call State Machine

Each call follows a strict lifecycle:

State	Description
IN_PROGRESS	Call streaming active
COMPLETED	Streaming finished
PROCESSING_AI	AI transcription running
FAILED	AI processing failed
ARCHIVED	Final state after success
🤖 AI Service Simulation

A mock transcription service is implemented to simulate real AI provider behavior:

✔ 25% random failure rate
✔ 1–3 second random latency
✔ Automatic retry with exponential backoff
✔ Fault tolerant background execution

🔄 Retry Strategy (Production Grade)

The system retries failed AI requests using:

Exponential backoff

Async task scheduling

Graceful error recovery

This prevents system failure during third-party outages.

🌐 Real-Time WebSocket Updates

Supervisors can monitor call processing live.

WebSocket provides:

Live status broadcast

Processing completion alerts

Error notifications

⚠ Concurrency Safety

Race conditions occur when two packets arrive simultaneously.

This project prevents corruption by using:

✔ PostgreSQL row-level locking
✔ SELECT FOR UPDATE strategy
✔ Transaction based commits

🧪 Integration Testing

A real concurrency test is implemented using:

pytest

httpx AsyncClient

asyncio.gather

This simulates two packets arriving at the exact same time.

🏗 System Architecture
Client
   │
   ▼
FastAPI Async API
   │
   ├── Packet Validation
   ├── Database Transaction
   ├── Background AI Task
   │
   ▼
PostgreSQL (Async)
   │
   ▼
AI Processing Layer (Mock)
   │
   ▼
WebSocket Broadcast

🧠 Design Principles Used

Non-blocking architecture

Separation of concerns

Async IO everywhere

Fault tolerance

Database consistency

Scalable microservice pattern

🛠 Technology Stack
Layer	Technology
Backend API	FastAPI
Async Server	Uvicorn
Database	PostgreSQL
ORM	SQLAlchemy Async
Driver	AsyncPG
Testing	Pytest + HTTPX
WebSockets	Starlette
Language	Python 3.11
📁 Project Structure
ai_pbx_backend/
│
├── app/
│   ├── main.py                 # FastAPI app & routes
│   ├── database.py             # Async DB connection
│   ├── models.py               # ORM models
│   ├── schemas.py              # Pydantic schemas
│   ├── ai_service.py           # Mock AI service
│   ├── retry.py                # Exponential retry logic
│   ├── websocket_manager.py    # WebSocket broadcast manager
│
├── tests/
│   ├── test_race_condition.py  # Concurrency test
│   ├── conftest.py
│
├── .gitignore
├── README.md
├── requirements.txt

⚙ Local Setup Guide
1️⃣ Clone Repository
git clone https://github.com/Mansoor-codess/ai-pbx-backend.git
cd ai-pbx-backend

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Linux / Mac:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ PostgreSQL Configuration

Create database:

CREATE DATABASE pbx_db;


Update database URL inside:

app/database.py


Example:

postgresql+asyncpg://postgres:password@localhost:5432/pbx_db

5️⃣ Run Backend Server
uvicorn app.main:app --reload


Server URL:

http://127.0.0.1:8000

📡 API Documentation

Swagger UI available at:

http://127.0.0.1:8000/docs

📤 Packet Ingestion Endpoint
POST
/v1/call/stream/{call_id}

Request Body
{
  "sequence": 1,
  "data": "audio chunk",
  "timestamp": 1.25
}

Response
202 Accepted

🔌 WebSocket Endpoint
ws://127.0.0.1:8000/ws


Used for real-time status streaming.

🧪 Running Tests

Execute:

pytest


Expected Output:

1 passed


This validates:

✔ Race condition handling
✔ Concurrent API requests
✔ Database locking behavior

🚦 Reliability Engineering

The backend ensures production-style reliability using:

Retry mechanism

Async background processing

Database transaction safety

Error state recovery

📊 Performance Considerations

Async IO based design

No blocking threads

Connection pooling

Lightweight request handling

Horizontal scaling friendly

🎓 Learning Outcomes

This project demonstrates:

✔ Async backend development
✔ Database concurrency control
✔ Microservice reliability patterns
✔ WebSocket implementation
✔ Testing async APIs
✔ Production design thinking

👨‍💻 Author

Mansoor Alam
FastAPI Backend Intern Evaluation Submission
Voice & AI Team