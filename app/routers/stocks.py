from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from .. import crud, schemas, services
from ..database import get_db
from ..redis_client import redis_client
import asyncio
import json

router = APIRouter()

@router.post("/stocks/", response_model=schemas.Stock)
async def add_stock(stock: schemas.StockCreate, db: AsyncSession = Depends(get_db)):
    db_stock = await crud.get_stock_by_symbol(db, symbol=stock.symbol)
    if db_stock:
        raise HTTPException(status_code=400, detail="Stock already registered")
    return await crud.create_stock(db=db, stock=stock)

@router.get("/stocks/{symbol}/indicators")
async def get_stock_indicators(symbol: str):
    cached_data = await redis_client.get(f"indicators:{symbol}")
    if cached_data:
        return json.loads(cached_data)
    data =  await services.get_stock_data(symbol)
    indicators = await services.calculate_indicators(data)

    await redis_client.setex(f"indicators:{symbol}", 3600, indicators.to_json())
    return indicators.to_dict()

@router.websocket("/ws/{symbol}")
async def websocket_endpoint(websocket: WebSocket, symbol: str):
    await websocket.accept()
    try:
        while True:
            data = await services.get_stock_data(symbol)
            latest_price = data["Close"].iloc[-1]
            await websocket.send_text(f"Latest price for {symbol}: {latest_price}")
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        print(f"Client disconnected from {symbol} websocket")

