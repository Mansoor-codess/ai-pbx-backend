# 🚀 AI-PBX Backend System — FastAPI Voice & AI Microservice

A high-performance asynchronous backend system designed to simulate an enterprise-grade PBX (Private Branch Exchange) AI routing service.  
This project demonstrates scalable API ingestion, fault-tolerant AI orchestration, database concurrency handling, and real-time WebSocket communication.

> **Submission Project — FastAPI Backend Intern (Voice & AI Team)**

---

## 📌 Problem Statement

Modern PBX systems handle thousands of concurrent calls. When human agents are unavailable, calls must be routed to AI voice bots.  
These AI services are often slow, unreliable, and prone to failures.

This project addresses:

- High-throughput packet ingestion  
- Maintaining packet order  
- Handling flaky AI APIs  
- Background AI processing  
- Database race condition handling  
- Real-time supervisor updates  

---

## 🎯 Project Objectives

- Accept streaming audio metadata asynchronously  
- Process AI transcription without blocking API responses  
- Maintain call lifecycle using a state machine  
- Handle concurrent database writes safely  
- Automatically recover from AI failures  
- Broadcast live processing updates  

---

## ⚙ Core Features

### 🚀 Asynchronous API Architecture
- Fully async FastAPI endpoints  
- Sub-50ms ingestion response target  
- Async SQLAlchemy database engine  

---

### 📦 Packet Streaming Validation
- Accepts streaming packet metadata  
- Sequence validation logic  
- Missing packet detection (warning logs)  
- Non-blocking request handling  

---

### 🔁 Call State Machine

Each call follows the lifecycle below:

| State | Description |
|------|------|
| IN_PROGRESS | Call streaming active |
| COMPLETED | Streaming finished |
| PROCESSING_AI | AI transcription running |
| FAILED | AI processing failed |
| ARCHIVED | Final archived state |

---

### 🤖 AI Service Simulation

A mock transcription service simulates real AI provider behavior:

- 25% random failure rate  
- 1–3 second random latency  
- Automatic retry with exponential backoff  
- Fault tolerant background execution  

---

### 🔄 Retry Strategy (Production Grade)

- Exponential backoff retry algorithm  
- Async retry scheduling  
- Automatic recovery from failures  
- Prevents manual intervention  

---

### 🌐 Real-Time WebSocket Updates

WebSocket channel enables:

- Live call status updates  
- Processing completion notifications  
- Error alerts for supervisors  

---

### ⚠ Concurrency Safety

Race conditions occur when packets arrive simultaneously.

Handled using:

- PostgreSQL row-level locking  
- `SELECT FOR UPDATE` strategy  
- Atomic database transactions  

---

### 🧪 Integration Testing

Concurrency is tested using:

- pytest  
- pytest-asyncio  
- httpx AsyncClient  
- asyncio.gather  

Simulates multiple packets arriving at the same time.

---

## 🏗 System Architecture

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
PostgreSQL (Async ORM)
│
▼
AI Processing Layer (Mock)
│
▼
WebSocket Broadcast


---

## 🧠 Design Principles

- Non-blocking architecture  
- Separation of concerns  
- Async IO everywhere  
- Fault tolerance  
- Database consistency  
- Scalable microservice design  

---

## 🛠 Technology Stack

| Layer | Technology |
|------|------|
| Backend API | FastAPI |
| ASGI Server | Uvicorn |
| Database | PostgreSQL |
| ORM | SQLAlchemy Async |
| Driver | AsyncPG |
| Testing | Pytest + HTTPX |
| WebSocket | Starlette |
| Language | Python 3.11 |

---

## 📁 Project Structure

ai_pbx_backend/
│
├── app/
│ ├── main.py # FastAPI app & routes
│ ├── database.py # Async DB connection
│ ├── models.py # ORM models
│ ├── schemas.py # Pydantic schemas
│ ├── ai_service.py # Mock AI service
│ ├── retry.py # Exponential retry logic
│ ├── websocket_manager.py # WebSocket manager
│
├── tests/
│ ├── test_race_condition.py # Concurrency integration test
│ ├── conftest.py
│
├── .gitignore
├── README.md
├── requirements.txt


---

## ⚙ Local Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Mansoor-codess/ai-pbx-backend.git
cd ai-pbx-backend

2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:
Windows
venv\Scripts\activate
Linux / Mac
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


Server will start at:

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


Used for real-time call updates.

🧪 Running Tests

Execute:

pytest


Expected output:

1 passed

This validates:

Concurrent packet ingestion

Database locking behavior

Race condition safety

🚦 Reliability Engineering

The backend ensures production reliability using:

Retry mechanisms

Async background processing

Transaction safety

Failure state recovery

📊 Performance Considerations

Async IO based design

No blocking threads

Connection pooling

Horizontal scaling friendly

🎓 Learning Outcomes

This project demonstrates:

Async backend engineering

Database concurrency control

Microservice reliability patterns

WebSocket implementation

Production-grade API design

Integration testing

👨‍💻 Author

Mansoor Alam
FastAPI Backend Intern Evaluation Submission
Voice & AI Team