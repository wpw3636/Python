import math
import random 
import matplotlib.pyplot as plt

#inputs
muA = 70
sigmaA = 8
muB = 85
sigmaB = 6
pA = 0.6
pB = 0.4
N = 5000

scores = []
for _ in range(int(N*pA)):
    scores.append(random.gauss(muA,sigmaA))
for _ in range(int(round(N*pB,0))):
    scores.append(random.gauss(muB,sigmaB))
for x in range(N):
    if scores[x] < 0:
        scores[x] = 0
    elif scores[x] > 100:
        scores[x] = 100
smean = sum(scores) / N
svar = 0
for x in range(N):
    r = (scores[x] - smean) ** 2 / (N - 1)
    svar += r
s = math.sqrt(svar)

print(f"Of the {N} students, the mean exam score was {round(smean,2)},\nvariance was {round(svar,2)},\nstandard deviation was {round(s,2)}.")

cutoff = 79.5
def wheretocut(cutoff):
    trueApredA = 0
    trueApredB = 0
    trueBpredA = 0
    trueBpredB = 0
    for x in range(int(N*pA)):
        if scores[x] < cutoff:
            trueApredA += 1
        else:
            trueApredB += 1
    for x in range(int(N*pA),N):
        if scores[x] < cutoff:
            trueBpredA += 1
        else:
            trueBpredB += 1
    accuracy = [100*(trueBpredB+trueApredA)/N, 100*trueApredB/N, 100*trueBpredA/N]
    return accuracy
print(f"Assume a cutoff of {cutoff}\nAccuracy: {round(wheretocut(cutoff)[0],2)}%\nFalse positive rate: {round(wheretocut(cutoff)[1],2)}%\nFalse negative rate: {round(wheretocut(cutoff)[2],2)}%")
tests = 10
accuracies = []
for cutoff in range(65,95):
    accuracies.append(wheretocut(cutoff)[0])
print(f"The integer cutoff with the highest accuracy is {accuracies.index(max(accuracies)) + 65}")  

plt.hist(scores, density = 1, bins = [0,5,15,20,25,30,35,40,45,50,55,60,65,70,75,80,90,95,100])
plt.xlabel("Exam score")
plt.ylabel("Portion of students")
plt.title(f"Distribution of exam scores in a sample (N = {N})")
plt.show()