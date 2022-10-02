sentens1 = input("write any suggestion: ")
sentens2 = input("write any suggestion: ")

splitedSent1 = sentens1.split()
splitedSent2 = sentens2.split()

commonWords = []

for i in range(len(splitedSent1)):
    for j in range(len(splitedSent2)):
        if splitedSent1[i] == splitedSent2[j]:
            commonWords.append(splitedSent1[i])

print("Similar words are: " , ", ".join(commonWords))