from .genre import Genre
from .actor import Actor
from .director import Director

class Movie:

    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
            self.__year = None
            self.__description = None
            self.__director = None
            self.__actorList = None
            self.__genreList = None
            self.__runtime = None
        if year == "" or type(year) is not int:
            self.__title = None
            self.__year = None
            self.__description = None
            self.__director = None
            self.__actorList = None
            self.__genreList = None
            self.__runtime = None
        else:
            self.__title = title.strip()
            self.__year = year
            self.__description = ""
            self.__director = Director
            self.__actorList = []
            self.__genreList = []
            self.__runtime = 0
            
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def year(self) -> str:
        return self.__year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, descr: str):
        self.__description = descr.strip()
    
    @property
    def director(self) -> Director:
        return self.__director
    
    @director.setter
    def director(self, director1: Director):
        self.__director = director1

    @property
    def actors(self) -> list:
        return self.__actorList

    @actors.setter
    def actors(self, value: Actor):
        self.__actorList.append(value)

    @property
    def genres(self) -> list:
        return self.__genreList

    @genres.setter
    def genres(self, value: Genre):
        self.__genreList.append(value)
    
    @property
    def runtime_minutes(self) -> int:
        return self.__runtime

    @runtime_minutes.setter
    def runtime_minutes(self, value: int):
        if value < 0:
            raise ValueError
        self.__runtime = value

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Movie):
            return False
        return (other.__title == self.__title) and (other.__year == self.__year)

    def __lt__(self, other):
        if (self.__title == other.__title):
            return self.__year < other.__year
        return self.__title < other.__title

    def __hash__(self):
        return hash(self.__title + str(self.__year))

    def add_actor(self, addActor: Actor):
        if (addActor not in self.__actorList):
            self.__actorList.append(addActor)

    def remove_actor(self, removeActor: Actor):
        if (removeActor in self.__actorList):
            self.__actorList.remove(removeActor)

    def add_genre(self, addGenre: Genre):
        if (addGenre not in self.__genreList):
            self.__genreList.append(addGenre)

    def remove_genre(self, removeGenre: Genre):
        if (removeGenre in self.__genreList):
            self.__genreList.remove(removeGenre)

class TestMovieMethods:

    def test_init(self):
        movie1 = Movie("Harry Potter", 2010)
        assert movie1.title == "Harry Potter"
        assert movie1.year == 2010
        movie1.description = "Wizard Movie"
        assert movie1.description == "Wizard Movie"
        movie1.director = Director("Ronald Weasley")
        assert movie1.director == Director("Ronald Weasley")
        assert movie1.actors == []
        movie1.actors = Actor("Hermione Granger")
        assert movie1.actors == [Actor("Hermione Granger")]
        movie1.actors = Actor("Rubius Hagrid")
        assert movie1.actors == [Actor("Hermione Granger"), Actor("Rubius Hagrid")]
        assert movie1.genres == []
        movie1.genres = Genre("Fantasy")
        assert movie1.genres == [Genre("Fantasy")]
        movie1.genres = Genre("Adventure")
        assert movie1.genres == [Genre("Fantasy"), Genre("Adventure")]
        assert movie1.runtime_minutes == 0
        movie1.runtime_minutes = 100
        assert movie1.runtime_minutes == 100
        assert repr(movie1) == "<Movie Harry Potter, 2010>"
        movie2 = Movie("Ronald Weasley", 2010)
        #assert movie1 == movie2
        assert movie1 == movie1
        assert movie1 < movie2
        movie3 = Movie("Ronald Weasley", 2011)
        assert movie2 < movie3
        movie1.add_actor(Actor("Severus Snape"))
        assert movie1.actors == [Actor("Hermione Granger"), Actor("Rubius Hagrid"), Actor("Severus Snape")]
        movie1.remove_actor(Actor("Severus Snape"))
        assert movie1.actors == [Actor("Hermione Granger"), Actor("Rubius Hagrid")]
        movie1.add_genre(Genre("Wizard"))
        assert movie1.genres == [Genre("Fantasy"), Genre("Adventure"), Genre("Wizard")]
        movie1.add_genre(Genre("Wizard"))
        assert movie1.genres == [Genre("Fantasy"), Genre("Adventure"), Genre("Wizard")]
        movie1.remove_genre(Genre("Wizard"))
        assert movie1.genres == [Genre("Fantasy"), Genre("Adventure")]
        movie1.director = Director("Albus Dumbledore")
        assert movie1.director == Director("Albus Dumbledore")
        assert hash(movie1) == hash(movie1)
        #assert hash(movie2) == hash(movie1)