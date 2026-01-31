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
2. Sequence order is validated
3. Data is stored asynchronously
4. When final packet arrives, AI processing is triggered in background
5. Results are saved and broadcasted via WebSocket

---

### AI Processing Flow

- External AI API is simulated with random latency and failure
- Automatic retry logic handles failures using exponential backoff
- Background task ensures API remains non-blocking
- Final transcription result updates database state

---

## ⚙ Tech Stack

- FastAPI (Async Backend)
- PostgreSQL (Async SQLAlchemy)
- SQLAlchemy ORM
- asyncpg driver
- WebSockets
- pytest + httpx
- Python 3.11

---

## 📦 Installation & Setup

### 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd ai_pbx_backend
