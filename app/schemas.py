from pydantic import BaseModel
from datetime import datetime

class StockBase(BaseModel):
    symbol: str
    name: str | None = None

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int
    last_price: float
    timestamp: datetime

    class Config:
        orm_mode = True
