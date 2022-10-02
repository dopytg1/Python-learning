import random
days = int(input("Enter number of days: "))
numOfLists = 3

exchanges = []

for i in range(numOfLists):
    listExch = []
    exchanges.append(listExch)

    for j in range(days):
        number = round(random.uniform(95, 100), 2)
        exchanges[i].append(number)

print(exchanges)
        

exchange1 = [97.33, 97.41, 99.55, 98.83]
exchange2 = [96.85, 98.49, 98.30, 98.77]
exchange3 = [99.15, 97.72, 90.0, 98.84]




exchangesPull = []
for i in range(len(exchanges)):
    exchangesPull += exchanges[i]


total = 0
for i in range(len(exchangesPull)):
    total += exchangesPull[i]

average = round(total/len(exchangesPull), 6)

print(average)