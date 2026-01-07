import random
import statistics as stat
import matplotlib.pyplot as plt

mu = 0.0005 #mean daily movement%
sigma = 0.02# #standard deviation of daily move
P = 100 #stock price
N = 252 #trading days

returnonday = []
for _ in range(N):
    returnonday.append(random.gauss(mu,sigma))

priceonday = [P]
for x in range(N - 1):
    P *= (1 + returnonday[x])
    priceonday.append(P)

meanreturn = stat.mean(returnonday)
stdevreturn = stat.stdev(returnonday)
startP = priceonday[0]
endP = priceonday[N - 1]
maxP = max(priceonday)
minP = min(priceonday)
maxgain = max(returnonday)
maxloss = min(returnonday)
print(f"Mean return: {round(100*meanreturn,2)}%\nStandard deviation of returns: {round(100*stdevreturn,2)}%\nBeginning price: ${round(startP,2)} on day 1\nEnding price: ${round(endP,2)} on day {N}\nHighest price: ${round(maxP,2)} on day {priceonday.index(maxP) + 1}\nLowest price: ${round(minP,2)} on day {priceonday.index(minP) + 1}\nBiggest gain: +{round(100*maxgain,2)}% on day {returnonday.index(maxgain) + 1}\nBiggest loss: {round(100*maxloss,2)}% on day {returnonday.index(maxloss) + 1}")

plt.plot(priceonday)
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Stock Price")
plt.show()