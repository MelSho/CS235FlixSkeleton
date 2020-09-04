from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__reviews: list = []
        self.__watched_movies = []
        self.__time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self) -> str:
        return self.__user_name
    
    @property
    def password(self) -> int:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies
    
    @property
    def reviews(self) -> list:
        return self.__reviews
    
    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return other.__user_name == self.__user_name
    
    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)
    
    def watch_movie(self, movie: Movie):
        if (movie not in self.__watched_movies):
            self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes
    
    def add_review(self, review):
        self.__reviews.append(review)

class TestUserMethods:

    def test_init(self):
        movie1 = Movie("Harry Potter", 2010)
        movie1.runtime_minutes = 100
        assert movie1.runtime_minutes == 100
        user1 = User("Hermione Granger", "hp100")
        assert user1.user_name == "hermione granger"
        assert user1.password == "hp100"
        assert user1.watched_movies == []
        assert user1.reviews == []
        assert user1.time_spent_watching_movies_minutes == 0
        user1.watch_movie(movie1)
        assert user1.watched_movies == [movie1]
        assert user1.time_spent_watching_movies_minutes == 100
        user1.add_review("wow so good i love harry potter")
        assert user1.reviews == ["wow so good i love harry potter"]
        