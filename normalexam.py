import math
import random
import matplotlib.pyplot as plt

# population distribution data
mu = 75 #test scores: 0 < mu < 100
sigma = 10
N = 1000

scores = []
for _ in range(N):
    r = random.gauss(mu,sigma)
    scores.append(r)
for x in range(N):
    if scores[x] < 0:
        scores[x] = 0
    elif scores[x] > 100:
        scores[x] = 100
smean = sum(scores) / N
svar = 0
for x in range(0,N):
    r = (scores[x] - smean) ** 2 / (N - 1)
    svar += r
s = math.sqrt(svar)
count1 = 0
for x in scores:
    if x > 90:
        count1 += 1
prob1 = count1 / N
count2 = 0
for x in scores:
    if 65 < x < 85:
        count2 += 1
prob2 = count2 / N
print(f"Of the {N} students, the mean exam score was {round(smean,2)},\nvariance was {round(svar,2)},\nstandard deviation was {round(s,2)},\n{round(100*prob1,2)}% scored above 90,\n{round(100*prob2,2)}% scored between 65 and 85.")

plt.hist(scores, density = 1, bins = [0,5,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,95,100])
plt.xlabel("Exam score")
plt.ylabel("Portion of students")
plt.title(f"Distribution of exam scores in a sample (N = {N})")
plt.show()
