from typing import Dict, List, Optional
import json

class Rating:
    def __init__(self, name: str, rate: int):
        self.name = name
        self.rate = int(rate)


class Movie:
    def __init__(self, name: str, ratings: Optional[List[Rating]]):
        self.name = name
        self.ratings = ratings
        total = 0
        for rate in ratings:
            total += rate.rate
        self.average = total / len(ratings) if bool(ratings) else 0

    def print_movie(self):
        print(f"{self.name:<30}{self.average:>35}")

    def print_movie_with_rates(self):
        print(self.name)
        print(f"{'Name:':<20}{'Rate:':>15}")

        for i in range(len(self.ratings)):
             print(f'{self.ratings[i].name:<20}{self.ratings[i].rate:>15}')

    def add_rate(self, add_rate):
        self.ratings.append(add_rate)
        total = 0
        for rate in self.ratings:
            total += rate.rate
        self.average = total / len(self.ratings) if bool(self.ratings) else 0

    def delete_rate(self, delete_rate):
        self.ratings.remove(delete_rate)
        total = 0
        for rate in self.ratings:
            total += rate.rate
        self.average = total / len(self.ratings) if bool(self.ratings) else 0

    def to_dict(self):
        ratings = {}
        for rating in self.ratings:
            ratings[rating.name] = rating.rate
        return {"name": self.name, "ratings": ratings, "average": self.average}


class MovieList:
    def __init__(self, movies: Optional[List[Movie]]):
        self.movies = movies
    
    def print_movies(self):
        print(f"{'Movies':<30}{'Average':>35}")
        print("-" * 65)
        for movie in self.movies:
            movie.print_movie()

    def add_movie(self, new_movie: Movie):
        self.movies.append(new_movie)

    def delete_movie(self, del_movie: Movie):
        self.movies.remove(del_movie)

    def get_movie(self, get_movie: str):
        for movie in self.movies:
            if get_movie == movie.name:
                return movie
        return False


class Application:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.movie_list = MovieList(self.read_from_file())
    
    def write_to_file(self):
        with open(self.file_path, 'w') as m:
            movies_data = []
            for movie in self.movie_list.movies:
                movies_data.append(movie.to_dict())
            json.dump(movies_data, m, indent=4)

    def read_from_file(self):
        with open(self.file_path, 'r') as m:
            movies_data = json.load(m)
            movies = []
            for movie_data in movies_data:
                movie_ratings = []
                for name, rating in movie_data['ratings'].items():
                    rate = Rating(name, rating)
                    movie_ratings.append(rate)
                movie = Movie(movie_data['name'], movie_ratings)
                movies.append(movie)
            return movies
    
    def find_movie(self):
        searchingFor = input("Searching for: ")
        movie =  self.movie_list.get_movie(searchingFor)
        if movie:
            movie.print_movie_with_rates()
        else:
            print("Movie not found")

    def add_movie(self):
        movie_name = input("name the movie: ")
        confirm = True
        for movie in self.movie_list.movies:
            if movie_name == movie.name:
                confirm = False
                break
            
        if confirm:
            newMovie = Movie(movie_name, {})
            self.movie_list.add_movie(newMovie)
            self.write_to_file()
        else:
            print("The movie already in list")

    def delete_movie(self):
        delete_movie = input("Delete: ")
        movie = self.movie_list.get_movie(delete_movie)
        if movie:
            confirm = input("You sure, you wanna delete it?")
            if confirm.lower().strip() in ('yes', 'y', 'ok'):
                self.movie_list.delete_movie(movie)
                self.write_to_file()
        else:
            print("The movie not found")

    def rate_movie(self):
        rateMovie = input("Name of the movie: ")
        movie = self.movie_list.get_movie(rateMovie)
       
        if movie:
                userName = input("Enter your name: ")
                userRate = int(input("Enter your rate: "))
                rating = Rating(userName, userRate)

                if userRate < 0 or userRate > 10:
                    print("rate should be between 0 and 10.Try again")
                    self.main()
                if userRate == 0:
                    for rating in movie.ratings:
                        if userName == rating.name:
                            movie.delete_rate(rating)
                            self.write_to_file()
                else:
                    movie.add_rate(rating)
                    self.write_to_file()
        else:
                print("Movie not found")

    def sort(self):
        self.movie_list.movies.sort(key = lambda item: item.average, reverse=True )
        print(self.movie_list.print_movies())


    def main(self):
        while True:
            command = input("Enter something from (list, find, add, delete, rate, sort or exit): ").lower().strip()
            if command == 'list':
                print("*" * 40)
                self.movie_list.print_movies()
            elif command == 'find':
                print("*" * 40)
                self.find_movie()
            elif command == 'add':
                print("*" * 40)
                self.add_movie()
            elif command == 'delete':
                print("*" * 40)
                self.delete_movie()
            elif command == 'rate':
                print("*" * 40)
                self.rate_movie()
            elif command == 'exit':
                break
            elif command == 'sort':
                self.sort()
            else:
                print("try again")
                pass
            
app = Application('movies.json')
app.main()