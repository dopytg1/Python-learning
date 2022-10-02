num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("yes")
else:
    print("no")