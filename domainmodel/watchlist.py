from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__WatchList = []

    @property
    def watch_list(self) -> list:
        return self.__WatchList
    
    def add_movie(self, movie: Movie):
        if (movie not in self.__WatchList):
            self.__WatchList.append(movie)
    
    def remove_movie(self, movie):
        if (movie in self.__WatchList):
            self.__WatchList.remove(movie)
    
    def select_movie_to_watch(self, index):
        if (index >= len(self.__WatchList)):
            return None
        else:
            return self.__WatchList[index]

    def size(self):
        return len(self.__WatchList)

    def first_movie_in_watchlist(self):
        if (len(self.__WatchList) == 0):
            return None
        else:
            return self.__WatchList[0]

    def __iter__(self):
        return self.__WatchList.__iter__()

    def __next__(self):
        if (len(self.__WatchList) == 0):
            raise StopIteration
        else:
            return self.__WatchList.pop(0)

class TestWatchListMethods:

    def test_init(self):
        movie1 = Movie("Harry Potter", 2010)
        movie2 = Movie("Ronald Weasley", 2010)
        movie3 = Movie("Hermione Granger", 2010)
        watchlist1 = WatchList()
        watchlist1.add_movie(movie1)
        watchlist1.add_movie(movie2)
        watchlist1.add_movie(movie3)
        assert watchlist1.watch_list == [movie1, movie2, movie3]
        watchlist1.remove_movie(movie3)
        assert watchlist1.watch_list == [movie1, movie2]
        towatch = watchlist1.select_movie_to_watch(0)
        assert towatch == movie1
        assert watchlist1.size() == 2
        first = watchlist1.first_movie_in_watchlist()
        assert first == movie1
