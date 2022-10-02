def counter():
    '''
    entering numbers, getting total of, getting average of
    no argument
    '''
    userNumbers = []
    print('Enter numbers: ')
    total = 0

    while True: #endless cycle adding numbers to list
        number = input("")
        if number == "end": #point of exit
            break

        userNumbers.append(int(number))

    for i in range(len(userNumbers)): #calculating the total sum of numbers
        total += userNumbers[i]

    entered = ""
    for i in range(len(userNumbers)):
        entered += str(userNumbers[i])
        if i == len(userNumbers) - 1:
            entered += "."
        else:
            entered += ", "


    print("You entered:", entered)
    print("Total:", total)
    print("Average:", total/len(userNumbers))

counter()