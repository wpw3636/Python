import random
import matplotlib.pyplot as plt
import statistics as stat

def experiment():
    toroll = [1,2,3,4,5,6]
    def rolled(x):
        return x in toroll
    rolls = 0
    while len(toroll) > 0:
        x = random.randint(1,6)
        rolls += 1
        if rolled(x) == True:
            toroll.remove(x)
    return rolls

N = 1000 #number of trials
datarolls = []
for _ in range(N):
    datarolls.append(experiment())

meanrolls = stat.mean(datarolls)
stdevrolls = stat.stdev(datarolls)
print(f"Number of experiments: {N}\nMean number of rolls: {meanrolls}\nStandard deviation of rolls: {stdevrolls}")

plt.hist(datarolls,bins = 50,range = (0,50))
plt.axvline(x=meanrolls,color = "r", lw = 0.5)
plt.xlabel("Number of rolls")
plt.ylabel("Frequency")
plt.title(f"Number of rolls observed in {N} trials")
plt.show()