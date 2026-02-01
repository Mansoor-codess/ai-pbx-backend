# AI PBX Backend – FastAPI Voice & AI Microservice

This project simulates a production-style PBX backend system that ingests real-time audio metadata, performs background AI transcription with retry handling, manages call state transitions, and broadcasts live updates via WebSockets.

It is designed to demonstrate asynchronous backend architecture, concurrency safety, and fault-tolerant AI orchestration.

---

## 🚀 Features Implemented

- Async FastAPI ingestion endpoint
- Non-blocking packet streaming (<50ms response)
- PostgreSQL async database integration
- Call state machine management
- Race condition safe packet handling
- Row-level locking for concurrency protection
- Flaky AI service simulation (25% failure rate)
- Exponential backoff retry strategy
- Background AI processing
- WebSocket real-time updates
- Integration testing with pytest + httpx

---

## 🏗 Architecture Overview

### Packet Ingestion Flow

1. Audio packets are sent to `/v1/call/stream/{call_id}`
2. Packet sequence order is validated
3. Data is stored asynchronously in PostgreSQL
4. API returns immediately with 202 Accepted
5. Processing continues in background

---

### AI Processing Flow

- External AI API is simulated with random latency and failure
- Automatic retry logic handles failures using exponential backoff
- Background task ensures API remains non-blocking
- Final transcription result updates database state
- WebSocket broadcasts status update

---

## 🔁 Call State Machine

Each call transitions through the following states:

- IN_PROGRESS  
- COMPLETED  
- PROCESSING_AI  
- FAILED  
- ARCHIVED  

State changes are safely handled inside database transactions.

---

## ⚙ Technology Stack

- FastAPI (Async Python Backend)
- PostgreSQL
- SQLAlchemy Async ORM
- asyncpg Driver
- WebSockets
- pytest + httpx
- Python 3.11
- Uvicorn ASGI Server

---

## 📂 Project Structure

```
ai_pbx_backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── ai_service.py
│   ├── retry.py
│   ├── websocket_manager.py
│
├── tests/
│   ├── test_race_condition.py
│   ├── conftest.py
│
├── .gitignore
├── README.md
├── requirements.txt


---

## 🛠 Setup Instructions (Local Environment)

### Step 1 — Clone Repository

```bash
git clone https://github.com/Mansoor-codess/ai-pbx-backend.git
cd ai-pbx-backend
```

---

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

### Step 3 — Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy asyncpg pytest httpx python-dotenv
```

---

### Step 4 — PostgreSQL Database Setup

Make sure PostgreSQL is running on port `5432`.

Create database:

```sql
CREATE DATABASE pbx_db;
```

Update database URL inside:

```
app/database.py
```

Example format:

```
postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/pbx_db
```

---

### Step 5 — Run Backend Server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Packet Ingestion Endpoint

```
POST /v1/call/stream/{call_id}
```

Request Body Example:

```json
{
  "sequence": 1,
  "data": "audio chunk",
  "timestamp": 1.25
}
```

Response:

```
202 Accepted
```

---

### WebSocket Endpoint

```
ws://127.0.0.1:8000/ws
```

Used to receive live processing updates.

---

## 🧪 Testing (Race Condition Simulation)

Run integration tests:

```bash
pytest
```

This test simulates:

- Two packets arriving at the same time
- Database locking behavior
- Concurrency handling
- Data consistency

Expected output:

```
1 passed
```

---

## ⚠ Reliability Handling

The mock AI transcription service simulates real-world instability:

- 25% failure probability
- Random latency between 1–3 seconds
- Automatic retry with exponential backoff
- Prevents manual retry intervention

---

## ⚡ Performance Design

- Fully asynchronous API endpoints
- Non-blocking database operations
- Background task execution
- Row-level locking for data safety
- Efficient async connection pooling

---

## 👨‍💻 Author

Mansoor Alam  
FastAPI Backend Intern Evaluation Submission  
Articence – Voice & AI Team
