
KEY_VALUE_DELIMETR = "****"
KEY_DIF_VALUE_DELIMETR = "&&&&"
KKKK = '||||'
DDDD = '####'


def read_from_file():
    movies = []
    with open('movie.txt', 'r') as m:
        movies_data = m.readlines()
        for movie_data in movies_data:
            movie_data = movie_data.strip()
            movie = {}
            for key_values in movie_data.split(KEY_DIF_VALUE_DELIMETR):
                key, value = key_values.split(KEY_VALUE_DELIMETR)
                movie[key] = value

            if movie['ratings'] != '':
                ratings_data = {}
                for key_values in movie['ratings'].split(DDDD):
                    key, values = key_values.split(KKKK)
                    ratings_data[key] = int(values)
                movie['ratings'] = ratings_data
            else:
                movie['ratings'] = {'rate': 0} #put a plug so that nothing breaks

            movies.append(movie)

    return movies


movies = read_from_file()


def write_to_file():
    movies_data = []
    for movie in movies:
        movie_data = []
        for key, value in movie.items():
            if type(value) == dict:
                rate_data = []
                rates_data = []
                for key, value in value.items():
                    rates_data.append(f'{key}{KKKK}{value}')
                rate_data.append(DDDD.join(rates_data))
                strRate = " ".join(rate_data)
                movie_data.append(f'ratings{KEY_VALUE_DELIMETR}{strRate}')
            else:
                movie_data.append(f'{key}{KEY_VALUE_DELIMETR}{value}')

        movies_data.append(KEY_DIF_VALUE_DELIMETR.join(movie_data))
    with open("movie.txt", "w") as m:
        m.write('\n'.join(movies_data))


def check_delimetr(text):
    for delimetr in (KEY_VALUE_DELIMETR, KEY_DIF_VALUE_DELIMETR, KKKK, DDDD):
        if delimetr in text:
            print(f"Don't enter {(KEY_VALUE_DELIMETR, KEY_DIF_VALUE_DELIMETR, KKKK, DDDD)}")
            return False
    return True


def average():
    for i in range(len(movies)):
        total = sum(movies[i]['ratings'].values())
        average = total/len(movies[i]['ratings'])
        movies[i]['average'] = average
        write_to_file()

average()

def find(text):
    search = input(text)

    for i in range(len(movies)):
        if search == movies[i]['name']:
            return movies[i]
    
    print("The film not founded in list")
    return False


def sort_by_name():
    def keyFunc(item):
        return item['name']

    movies.sort(key = keyFunc, reverse=False)
    write_to_file()


def sort_by_average():
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
    if check_delimetr(name):
        for i in range(len(movies)):
            for key, values in movies[i].items():
                if name == values:
                    confirm = True

        if not confirm:
            addThis['name'] = name
            addThis['average'] = 0
            movies.append(addThis)
            write_to_file()
        else:
            print("The movie already in list")


def list_film():
    sort_by_name()
    for i in range(len(movies)):
        total = sum(movies[i]['ratings'].values())
        if total != 0:
            print("%-25s %s" %(movies[i]['name'], total/len(movies[i]['ratings'])))
        else:
            print("%-25s %s" %(movies[i]['name'], "Film not rated"))


def find_film():
    search = find("Search for: ")

    print(f"Name: {search['name']}")
    if bool(search['ratings']):
        for a in search['ratings']:
            print("%-20s %s" %(a, search['ratings'][a]))
        print("%-20s %s" %("Average:", search['average']))
    else:
        print("Film not rated.")
        

def delete_film():
    search = find("Delete: ")

    if search != False:
        movies.remove(search)
        write_to_file()


def rate_film():
    try:
        film_to_rate = find("Name of the film:")

        if film_to_rate != False:
            nameUser = input("Enter your name: ")
            userRate = int(input("Enter your rate: "))
            if userRate < 0 or userRate > 10:
                print("rate should be between 0 and 10.Try again")
                rate_film()
            elif userRate == 0:
                del film_to_rate['ratings'][nameUser]
                write_to_file()
            else:
                film_to_rate['ratings'][nameUser] = userRate
                del film_to_rate['ratings']['rate']
                average()
                write_to_file()
        else:
            rate_film()
    except:
        print("error. Rate must be a number")


def main():
    while True:
        command = input("Enter something from (list, find, add, delete, rate, sort or exit): ").lower().strip()

        if command == 'list':
            print("*" * 40)
            list_film()
        elif command == 'find':
            print("*" * 40)
            find_film()
        elif command == 'add':
            print("*" * 40)
            add_film()
        elif command == 'delete':
            print("*" * 40)
            delete_film()
        elif command == 'rate':
            print("*" * 40)
            rate_film()
        elif command == 'exit':
            break
        elif command == 'sort':
            sort_by_average()
        else:
            print("try again")
            pass

main()