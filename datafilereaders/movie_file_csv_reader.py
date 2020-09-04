import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_movies: list = []
        self.dataset_of_actors: set = set()
        self.dataset_of_directors: set = set()
        self.dataset_of_genres: set = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                self.dataset_of_movies.append(Movie(title, release_year))
                actors = row['Actors']
                actors = actors.split(",")
                for x in range(0, len(actors)):
                    actors[x] = actors[x].strip()
                    if (actors[x] not in self.dataset_of_actors):
                        self.dataset_of_actors.add(Actor(actors[x]))
                directors = row['Director']
                if (directors not in self.dataset_of_directors):
                    self.dataset_of_directors.add(Director(directors))
                genres = row['Genre']
                genres = genres.split(",")
                for x in range(0, len(genres)):
                    genres[x] = genres[x].strip()
                    if (genres[x] not in self.dataset_of_genres):
                        self.dataset_of_genres.add(Genre(genres[x]))
                #print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1