import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

#inputs
ticker = 'AAPL' #Enter ticker of a stock here
startdate = '2021-01-01' #Enter starting date in format YYYY-MM-DD
enddate = '2025-12-31' #Enter ending date in format YYYY-MM-DD

data0 = yf.download(ticker, start=startdate, end=enddate)['Close']
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

plt.plot(date, data, lw = 1, label = ticker)
plt.plot(date, shortMA, lw = 1, label = "20 day moving average")
plt.plot(date, longMA, lw = 1, label = "100 day moving average")
plt.legend()
plt.xticks(fontsize = 8)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(ticker)
plt.show()
