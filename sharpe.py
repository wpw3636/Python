import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

#inputs
ticker = "SPY" #Enter ticker of a stock here
startdate = "2024-10-01" #Enter starting date in format YYYY-MM-DD (The chart will actually start 90 days after this date)
enddate = "2025-12-31" #Enter ending date in format YYYY-MM-DD

data0 = yf.download(ticker, start=startdate, end=enddate)["Close"]
data = np.array([])
for x in data0[ticker]:
    data = np.append(data,x)
date = np.array(data0.index)
date = date[90:]

rates0 = yf.download("^IRX", start=startdate, end=enddate)["Close"]

rates = []
for x in range(90,len(rates0)):
    rates.append(0.01*np.mean(rates0[x-90:x]))

returns = []
for x in range(90,len(data)):
    returns.append((data[x]-data[x-90])/data[x-90])

sigma = np.std(returns,ddof=1)

sharpes = []
for x in range(0,len(returns)):
    sharpes.append((returns[x]-rates[x])/sigma)

plt.plot(date, sharpes, lw = 1)
plt.axhline(color = "k", lw = 0.5)
plt.axhline(y = 1, color = "g", lw = 0.5)
plt.axhline(y = -1, color = "r", lw = 0.5)
plt.xticks(fontsize = 5)
plt.xlabel("Date")
plt.ylabel("90 day sharpe")
plt.title(f"{ticker} 90 day sharpe ratio")
plt.show()
