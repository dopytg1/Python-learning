str1 = len(input("Enter first string: "))
str2 = len(input("Enter second string: "))

if str1 > str2:
    longerBy = str1 - str2
    print("First string is longer by %s characters." % longerBy)
elif str1 < str2:
    longerBy = str2 - str1
    print("Second string is longer by %s characters." % longerBy)
else:
    print("Strings are equal length.")