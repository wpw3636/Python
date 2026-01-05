import random
import math
import matplotlib.pyplot as plt

N = 1000 #adjust the number of dice rolls in the experiment
rolls = []
for _ in range(1,1 + N):
    roll = random.randint(1,6)
    rolls.append(roll)
counts = []
for x in range(1,7):
    counts.append(rolls.count(x))
probs = []
for x in range(0,6):
    probs.append(counts[x] / N)
mean = 0
for x in range(0,6):
    mean += probs[x] * (x+1)
mode = probs.index(max(probs)) + 1
var = 0
for x in range(0,6):
    var += ((x + 1) - mean) ** 2 * probs[x]
stdev = math.sqrt(var)

print("Occurances of each dice roll:")
for x in range(0,6):
    print(f"{x+1}: {counts[x]}")
print(f"Mean: {mean}")
print(f"Mode: {mode}")
print(f"Standard deviation: {stdev}")

plt.bar(range(1,7),probs)
plt.xlabel("Number rolled")
plt.ylabel("Probability")
plt.title(f"Dice roll probabilities (N = {N})")
plt.show() #displays a probability mass function for the experiment