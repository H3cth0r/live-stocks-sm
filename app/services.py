import yfinance as yf
import pandas as pd
import ta

async def get_stock_data(symbol: str):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1y")
    return hist

async def calculate_indicators(data: pd.DataFrame):
    data['RSI'] = ta.momentum.RSIIndicator(data['Close']).rsi()
    data['SMA_20'] = ta.trend.SMAIndicator(data['Close'], window=20).sma_indicator()
    return data
