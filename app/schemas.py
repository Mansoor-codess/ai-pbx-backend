from pydantic import BaseModel

class Packet(BaseModel):
    sequence: int
    data: str
    timestamp: float
