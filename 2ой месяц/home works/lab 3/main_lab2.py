from random import randint


def get_input(text):
    answer = input(text).lower()
    if answer == 'exit':
        exit()
    return answer


def player_turn():
    randNum = randint(1, 100)
    i = 0
    while True:
        userAnsw = int(input("Try ro guess the number: "))
        i += 1

        if userAnsw == randNum:
            print("You got it right")
            print("Total moves %s" %i)
            return i
        elif userAnsw > randNum:
            print("Lower")
        elif userAnsw < randNum:
            print("Greater")


def computer_turn():
    i = 0
    greatStep = 100
    lowStep = 1

    while True:
        randomNum = randint(lowStep, greatStep)
        i += 1
        print("greater/less or yes: ")
        playerAnswer = get_input("Is it %s: " %(randomNum))
        
        if playerAnswer == 'less':
            greatStep = randomNum - 1
        elif playerAnswer == 'greater':
            lowStep = randomNum + 1
        elif playerAnswer == 'yes':
            print("Total %s moves" %i)
            return i

try:
    rounds = int(input("How much rounds do you want? "))
except:
    rounds = 3


winsComputer = 0
winsPlayer = 0
i = 0

while rounds > 0:
    i += 1

    print("-" * 40)
    print("It's your turn!!!\nGive your best!!!!")
    print("Round number: %s" %i)
    totalPlayer = player_turn()


    print("-" * 40)
    print("It's now a computer's turn. Watch out!!")
    print("Round number: %s" %i)
    totalComputer = computer_turn()

    if totalPlayer > totalComputer:
        winsComputer += 1
    else:
        winsPlayer += 1

    rounds -= 1

print("-" * 40)
if winsComputer > winsPlayer:
    print("Unfortuantly. You loose")
    print("The score is (%s : %s)" %(winsComputer, winsPlayer))
elif winsComputer == winsPlayer:
    print("Draw")
    print("The score is (%s : %s)" %(winsComputer, winsPlayer))
elif winsComputer < winsPlayer:
    print("Congratulations!!! You won")
    print("The score is (%s : %s)" %(winsComputer, winsPlayer))