import random

mu = 0.0005 #mean daily movement%
sigma = 0.02# #standard deviation of daily move
P = 100 #stock price
N = 252 #trading days

def simulate(mu,sigma,P,N):
    returnonday = []
    for _ in range(N):
        returnonday.append(random.gauss(mu,sigma))
    priceonday = [P]
    for x in range(N - 1):
        P *= (1 + returnonday[x])
        priceonday.append(P)
    return [returnonday,priceonday]

finalreturn = -0.1 #percent return 
tests1 = 10000
def probreturn(finalreturn,tests1):
    cutoff = P * (1 + finalreturn)
    count = 0
    if finalreturn >= 0:
        for _ in range(tests1):
            if simulate(mu,sigma,P,N)[1][N-1] > cutoff:
                count += 1
    else:
        for _ in range(tests1):   
            if simulate(mu,sigma,P,N)[1][N-1] < cutoff:
                count += 1
    return count / tests1
if finalreturn >= 0:
    print(f"The probability that the stock is up more than {100*finalreturn}% after {N} days is {probreturn(finalreturn,tests1)}")
else:
    print(f"The probability that the stock is down more than {100*finalreturn}% after {N} days is {probreturn(finalreturn,tests1)}")

dayreturn = 0.01
tests2 = 10000
def probdayreturn(dayreturn):
    values = simulate(mu,sigma,P,tests2)[0]
    count = 0
    if dayreturn >= 0:
        for x in range(tests2 - 1):
            if values[x] > dayreturn:
                count += 1
    else:
        for x in range(tests2 - 1):
            if values[x] < dayreturn:
                count += 1
    return count / tests2
if dayreturn >= 0:
    print(f"The probability that the stock gains more than {100*dayreturn}% in a day is {probdayreturn(dayreturn)}")
else:
    print(f"The probability that the stock loses more than {100*dayreturn}% in a day is {probdayreturn(dayreturn)}")