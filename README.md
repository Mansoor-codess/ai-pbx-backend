# AI PBX Backend Microservice (FastAPI)

This project is a backend microservice built using FastAPI that simulates a PBX system routing calls to an AI Voice-Bot when agents are unavailable. The system is designed to handle high concurrency, unreliable AI services, and real-time updates.

---

## 🚀 Features Implemented

- Asynchronous packet ingestion with FastAPI
- Non-blocking API response (<50ms)
- Packet sequence validation
- PostgreSQL async database integration
- Call lifecycle state management
- Mock AI transcription service with failures
- Exponential backoff retry handling
- WebSocket real-time broadcast
- Race condition handling using row-level locking
- Integration testing with pytest and httpx

---

## 🏗 Architecture Overview

### Flow:

1. Client sends audio packet metadata to FastAPI endpoint
2. Backend validates packet order
3. Call data is stored asynchronously in PostgreSQL
4. AI processing is simulated in background
5. Retry mechanism handles AI failures
6. WebSocket sends real-time updates to connected clients

---

## 🔁 Call State Machine

Each call follows the below lifecycle:

- IN_PROGRESS  
- COMPLETED  
- PROCESSING_AI  
- FAILED  
- ARCHIVED  

State transitions are handled safely inside database transactions.

---

## ⚙ Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy Async ORM
- AsyncPG Driver
- WebSockets
- Pytest
- HTTPX Async Client
- Uvicorn ASGI Server

---

## 📦 Project Structure

ai_pbx_backend/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── ai_service.py
│ ├── retry.py
│ ├── websocket_manager.py
│
├── tests/
│ ├── test_race_condition.py
│ ├── conftest.py
│
├── .gitignore
├── README.md
├── requirements.txt




---

## 🛠 Setup Instructions (Local Run)

### Step 1 — Clone Repository

```bash
git clone https://github.com/Mansoor-codess/ai-pbx-backend.git
cd ai-pbx-backend


Step 2 — Create Virtual Environment
python -m venv venv
Activate:

Windows:

venv\Scripts\activate


Linux / Mac:

source venv/bin/activate

Step 3 — Install Dependencies
pip install fastapi uvicorn sqlalchemy asyncpg pytest httpx python-dotenv

Step 4 — PostgreSQL Setup

Create database:

CREATE DATABASE pbx_db;


Update database connection string in:

app/database.py


Example:

postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/pbx_db

Step 5 — Run Server
uvicorn app.main:app --reload


Server will start at:
http://127.0.0.1:8000

📡 API Usage
Packet Ingestion Endpoint
POST /v1/call/stream/{call_id}


Sample JSON:

{
  "sequence": 1,
  "data": "audio chunk",
  "timestamp": 1.23
}


Response:

202 Accepted

WebSocket Endpoint
ws://127.0.0.1:8000/ws


Used for real-time call processing updates.

🧪 Testing (Race Condition Simulation)

Run:

pytest


This test simulates:

Two packets arriving at same time

Database locking behavior

Concurrent request handling

Expected Output:

1 passed

⚠ Reliability Handling

The mock AI transcription service:

Has 25% failure probability

Random latency between 1–3 seconds

Automatic retry using exponential backoff

Prevents manual intervention

📈 Performance Design

Fully async FastAPI endpoints

Non-blocking database queries

Background AI processing

Efficient connection pooling

Row-level locking for consistency

👨‍💻 Author

Mansoor Alam
FastAPI Backend Intern Evaluation Submission
Articence – Voice & AI Team
