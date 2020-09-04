from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie

def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    #print(movie_file_reader.dataset_of_movies())
    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    print(f'number of unique movies: {movie_file_reader.dataset_of_movies}')
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    print(f'number of unique actors: {movie_file_reader.dataset_of_actors}')
    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    print(f'number of unique directors: {movie_file_reader.dataset_of_directors}')
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
    print(f'number of unique genres: {movie_file_reader.dataset_of_genres}')
    
    #print(len(movie_file_reader.dataset_of_movies()))
    #print(movie_file_reader.dataset_of_actors())
    #print(len(movie_file_reader.dataset_of_actors()))
    #print(movie_file_reader.dataset_of_directors())
    #print(len(movie_file_reader.dataset_of_directors()))
    #print(movie_file_reader.dataset_of_genres())
    #print(len(movie_file_reader.dataset_of_genres()))


if __name__ == "__main__":
    main()