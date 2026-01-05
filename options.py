import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))
    C = S * norm.cdf(d1) - K * np.e ** (-r * T) * norm.cdf(d2)
    return C

# Inputs
S = 180
K = 185
T = 30 / 365
r = 0.04
sigma = 0.25

price = black_scholes_call(S, K, T, r, sigma)
print(f"Call Option Price: ${price:.2f}")

import matplotlib.pyplot as plt

vols = np.linspace(0.1, 0.6, 20) # What does linspace do?
prices = [black_scholes_call(S, K, T, r, v) for v in vols]

plt.plot(vols, prices)
plt.xlabel("Volatility")
plt.ylabel("Call Option Price")
plt.title("Call Option Price vs Volatility")
plt.show()
