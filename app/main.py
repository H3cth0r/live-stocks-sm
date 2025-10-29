from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import stocks

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(stocks.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Stock Analysis API"}
