from functools import total_ordering
from re import L

movies = [
    {
    'name': 'Interstellar',
    'ratings': {
            'John': 10,
            'Jack': 3
        }
    },
    {
    'name': 'Avengers: Infinity War',
    'ratings': {
            'Jack': 9,
            'Jane': 10
        }
    },
    {
    'name': 'Avengers: Infinity War',
    'ratings': {
            'Jack': 4,
            'Jane': 10
        }
    },
    {
    'name': 'Avengers: Infinity War',
    'ratings': {
            'Jack': 1,
            'Jane': 1
        }
    }
]

def average():
    for i in range(len(movies)):
        total = sum(movies[i]['ratings'].values())
        average = total/len(movies[i]['ratings'])

        movies[i]['average'] = average
average()

def find(text):
    search = input(text)

    for i in range(len(movies)):
        if search == movies[i]['name']:
            return movies[i]




def sort():
    def keyFunc(item):
        return item['average']

    movies.sort(key = keyFunc, reverse=True)
    for i in range(len(movies)):
        print("%-30s %s" %(movies[i]['name'], movies[i]['average']))


def add_film():
    name = input("name the film: ")
    addThis = {
        'name': '',
        'ratings': {}
    }
    confirm = 0
    for i in range(len(movies)):
        for key, values in movies[i].items():
            if name == values:
                confirm = True

    if not confirm:
        addThis['name'] = name
        addThis['average'] = 0
        movies.append(addThis)
    else:
        print("The movie already in list")


def list_film():
     for i in range(len(movies)):
        total = sum(movies[i]['ratings'].values())
        if total != 0:
            print("%-25s %s" %(movies[i]['name'], total/len(movies[i]['ratings'])))
        else:
            print("%-25s %s" %(movies[i]['name'], "Film not rated"))


def find_film():
    search = input("Search for: ")

    for i in range(len(movies)):
        total = sum(movies[i]['ratings'].values())

        if search == movies[i]['name']:
            print(movies[i]['name'])
            if bool(movies[i]['ratings']):
                for a in movies[i]['ratings']:
                    print("%-10s %s" %(a, movies[i]['ratings'][a]))
                print("average rating:", total/len(movies[i]['ratings']))
            else:
                print("Film not rated.")
        

def delete_film():
    search = input("Delete: ")

    for i in range(len(movies)):
        if search == movies[i]['name']:
            del movies[i]
            break
        elif search not in movies[i].items():
            print("The film not founded in list")


def rate_film():
    try:
        film_to_rate = find("Name of the film:")
        nameUser = input("Enter your name: ")
        userRate = int(input("Enter your rate: "))

        if userRate < 0 or userRate > 10:
            print("rate should be between 0 and 10.Try again")
            rate_film()
        elif userRate == 0:
            del film_to_rate['ratings'][nameUser]
        else:
            film_to_rate['ratings'][nameUser] = userRate
            average()
    except:
        print("error. Rate must be a number")




while True:
    command = input("Enter something from (list, find, add, delete, rate, sort or exit): ")

    if command == 'list':
        list_film()
    elif command == 'find':
        find_film()
    elif command == 'add':
        add_film()
    elif command == 'delete':
        delete_film()
    elif command == 'rate':
        rate_film()
    elif command == 'exit':
        break
    elif command == 'sort':
        sort()
    else:
        print("try again")
        pass