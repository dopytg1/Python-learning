from random import randint


def get_input(text):
    answer = input(text).lower()
    if answer == 'exit':
        exit()
    return answer


def game_1():
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
            break


def game_2():
    randNum = randint(1, 100)
    i = 0
    while True:
        userAnsw = int(input("Try ro guess the number: "))
        i += 1

        if userAnsw == randNum:
            print("You got it right")
            print("Total moves %s" %i)
            break
        elif userAnsw > randNum:
            print("Lower")
        elif userAnsw < randNum:
            print("Greater")


while True:
    userChoose = get_input("Choose the game you would like to play. Type 1 or 2: ")

    if userChoose == "1":
        game_1()
    elif userChoose == "2":
        game_2()