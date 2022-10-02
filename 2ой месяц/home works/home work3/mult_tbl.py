from random import randint

mult1 = randint(1, 9)
mult2 = randint(1, 9)

correctAnsw = mult1 * mult2
userAnsw = input("How much is %s * %s?: " % (mult1, mult2))

if int(userAnsw) == correctAnsw:
    print("Correct")
else: 
    print("Wrong. Correct answer is: %s" % (correctAnsw))