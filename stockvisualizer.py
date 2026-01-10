import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

ticker = 'AAPL' #Enter ticker of a stock here
data0 = yf.download(ticker, start="2021-01-01", end="2025-12-31")['Close']
data = np.array(data0)
date = np.array(data0.index)

shortMA = np.array([])
for n in range(len(data)):
    if n < 20:
        shortMA = np.append(shortMA,[np.nan])
    else:
        x = 0
        for z in range(20,0,-1):
            x += data[n - z]
        shortMA = np.append(shortMA,[x/20])

longMA = np.array([])
for n in range(len(data)):
    if n < 100:
        longMA = np.append(longMA,[np.nan])
    else:
        x = 0
        for z in range(100,0,-1):
            x += data[n - z]
        longMA = np.append(longMA,[x/100])

plt.plot(date, data, label = ticker)
plt.plot(date, shortMA, label = "20 day moving average")
plt.plot(date, longMA, label = "100 day moving average")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(ticker)
plt.show()