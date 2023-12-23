from pydantic import BaseModel
from datetime import datetime


class SensorDataIn(BaseModel):
    temperature: float
    humidity: float
    preassure: float
    timestamp: datetime


class SensorData(SensorDataIn):
    id: int
