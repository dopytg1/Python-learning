from random import randint

i = 0
greatStep = 100
lowStep = 1

while True:
    randomNum = randint(lowStep, greatStep)
    i += 1
    print("greater/less or yes: ")
    playerAnswer = input("Is it %s: " %(randomNum))
    
    if playerAnswer == 'less':
        greatStep = randomNum - 1
    elif playerAnswer == 'greater':
        lowStep = randomNum + 1
    elif playerAnswer == 'yes':
        print("Total %s moves" %i)
        break