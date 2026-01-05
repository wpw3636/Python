import numpy as np
import yfinance as yf
import pandas as pd

def historical_vol(ticker):
    data = yf.download(ticker, start="2025-01-01", end="2025-12-31")
    daily_change = (data['Close'] - data['Open'])/data['Open']
    daily_standev = (np.std(daily_change, axis = 0))[ticker]
    year_standev = (daily_standev * np.sqrt(len(data)))
    monthly_standev = (year_standev / np.sqrt(12))
    print(ticker, "2025 daily volatility:", round(daily_standev * 100, 2),"%")
    print(ticker, "2025 monthy volatility:", round(monthly_standev * 100, 2),"%")
    print(ticker, "2025 annualized volatility:", round(year_standev * 100, 2),"%")

historical_vol('AAPL') #Enter the ticker of a stock and the program will return it's average daily, monthly, and overall annualized volatility from 2025
