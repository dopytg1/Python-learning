# num1 = int(input("Enter the first num: "))  # Didn't know which one was correct so left both
# num2 = int(input("Enter the second num: "))

nums = input("Enter two nums with a space between them: ")

num1 = int(nums[0])
num2 = int(nums[2])

print(num1, num2)
if num1 == num2:
    print("=")
elif num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
else:
    print("error")