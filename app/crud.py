from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas
from datetime import datetime

async def get_stock_by_symbol(db: AsyncSession, symbol: str):
    result = await db.execute(select(models.Stock).filter(models.Stock.symbol == symbol))
    return result.scalars().first()

async def create_stock(db: AsyncSession, stock: schemas.StockCreate):
    db_stock = models.Stock(**stock.dict(), last_price=0.0, timestamp=datetime.utcnow())
    db.add(db_stock)
    await db.commit()
    await db.refresh(db_stock)
    return db_stock
