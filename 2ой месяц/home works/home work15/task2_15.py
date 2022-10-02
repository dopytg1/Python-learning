height = int(input("Input pyramid height: "))

h = 1
widht = height - 1

for i in range(height):
    space = " "
    space *= widht
    elementToPrint = "*"
    elementToPrint *= h
    k = space + elementToPrint
    print(k)

    h += 2
    widht -= 1