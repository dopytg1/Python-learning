radii = [12, 35, 4]
areas = []

def count_squere():
    constS = 3.14
    for i in range(len(radii)):
        areas.append((radii[i]**2) * constS)

    print(areas)    

count_squere()