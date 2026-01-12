import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#inputs
ticker = 'JPM' #Enter ticker of a stock here
startdate = '2021-01-01' #Enter starting date in format YYYY-MM-DD
enddate = '2025-12-31' #Enter ending date in format YYYY-MM-DD

data0 = yf.download(ticker, start=startdate, end=enddate)['Close']
data = np.array([])
for x in data0[ticker]:
    data = np.append(data,x)
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

cash = 10000
shares = 0
cashaccount = np.array([])
stockaccount = np.array([])
shareaccount = np.array([])

for x in range(len(data)):
    if np.isnan(longMA[x]) == True:
        cashaccount = np.append(cashaccount, cash)
        shareaccount = np.append(shareaccount, shares)
        stockaccount = np.append(stockaccount, shares*data[x])
    elif shortMA[x] > longMA[x] and shares == 0:
        shares = cash / data[x]
        cash = 0
        cashaccount = np.append(cashaccount, cash)
        shareaccount = np.append(shareaccount, shares)
        stockaccount = np.append(stockaccount, shares*data[x])
    elif shortMA[x] < longMA[x] and shares > 0:
        cash = shares * data[x]
        shares = 0
        cashaccount = np.append(cashaccount, cash)
        shareaccount = np.append(shareaccount, shares)
        stockaccount = np.append(stockaccount, shares*data[x])
    else:
        cashaccount = np.append(cashaccount, cash)
        shareaccount = np.append(shareaccount, shares)
        stockaccount = np.append(stockaccount, shares*data[x])
portfolio = np.maximum(cashaccount,stockaccount)

stockreturnsince0 = np.array([])
for x in range(len(data)):
    r = 100 * (data[x]-data[0])/data[0]
    stockreturnsince0 = np.append(stockreturnsince0,r)

portfolioreturnsince0 = np.array([])
for x in range(len(data)):
    r = 100 * (portfolio[x]-portfolio[0])/portfolio[0]
    portfolioreturnsince0 = np.append(portfolioreturnsince0,r)

info = np.array([[data[0],data[len(data)-1],data[len(data)-1]-data[0],stockreturnsince0[len(data)-1]],
                 [portfolio[0],portfolio[len(data)-1],portfolio[len(data)-1]-portfolio[0],portfolioreturnsince0[len(data)-1]]])
info = info.round(2)
df = pd.DataFrame(info, columns = ["$ start","$ end","$ change","% change"], index = [ticker,"crossover strategy"])
print(df)

plt.plot(date, portfolioreturnsince0, lw = 1, label = "Crossover Strategy")
plt.plot(date, stockreturnsince0, lw = 1, label = ticker)
plt.legend()
plt.axhline(color = "k", lw = 1)
plt.xticks(fontsize = 8)
plt.xlabel("Date")
plt.ylabel("Percent change")
plt.title(f"{ticker} vs moving average crossover strategy")
plt.show()