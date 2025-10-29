from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stock(Base):
    __tablename__ = "stocks"

    id          = Column(Integer, primary_key=True, index=True)
    symbol      = Column(String, unique=True, index=True)
    name        = Column(String)
    last_price  = Column(Float)
    timestamp   = Column(DateTime)
