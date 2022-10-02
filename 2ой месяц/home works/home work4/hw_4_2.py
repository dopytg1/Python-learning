import math


def average_mark():
    names = ["Bill", "Jane", "John", "Mary"]
    marks = []
    marksSum = 0

    for i in range(len(names)): # adding marks to students
        mark = int(input("Enter mark for %s: " % names[i])) #using list of names to designate the students
        marks.append(mark)

        marksSum += marks[i]

    print("Average mark: %s" %(math.ceil(marksSum/len(marks))))


average_mark()