from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()

class CallState(enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    PROCESSING_AI = "PROCESSING_AI"
    FAILED = "FAILED"
    ARCHIVED = "ARCHIVED"


class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True)
    call_id = Column(String, unique=True)
    last_sequence = Column(Integer, default=0)
    state = Column(Enum(CallState), default=CallState.IN_PROGRESS)
    transcription = Column(String, nullable=True)
