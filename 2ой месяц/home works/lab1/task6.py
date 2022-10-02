import random

amountOfNums = 10

randNums = [[], []]
sumNums = []

for i in range(2):
    for j in range(amountOfNums):
        randNums[i].append(random.randint(0, 100))

max = randNums[0][0] + randNums[0][1]
for i in range(amountOfNums):
    sumNums.append(randNums[0][i] + randNums[1][i])
    if max < sumNums[i]:
        max = sumNums[i]
    else:
        continue

print(randNums[0])
print(randNums[1])
print(sumNums)
print(max)