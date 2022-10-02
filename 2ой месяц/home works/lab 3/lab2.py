from random import randint

randNum = randint(1, 100)

print(randNum)
while True:
    userAnsw = int(input("Try ro guess the number: "))

    if userAnsw == randNum:
        print("You got it right")
        break
    elif userAnsw > randNum:
        print("Lower")
    elif userAnsw < randNum:
        print("Greater")