from datetime import datetime
import time
from domainmodel.movie import Movie

class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
        if type(rating) is not int:
            self.__rating = None
        else:
            if rating > 10 or rating < 1:
                self.__rating = None
            else:
                self.__rating = rating
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        self.__timestamp = datetime.now()

    @property
    def review_text(self) -> str:
        return self.__review_text
    
    @property
    def rating(self) -> int:
        return self.__rating
    
    @property
    def movie(self) -> Movie:
        return self.__movie
    
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"Review of {self.__movie} at {self.__timestamp}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Review):
            return False
        return ((other.__movie == self.__movie) and (other.__review_text == self.__review_text) and (other.__rating == self.__rating) and (other.__timestamp == self.__timestamp))

class TestReviewMethods:

    def test_init(self):
        movie1 = Movie("Harry Potter", 2010)
        review1 = Review(movie1, "amazing", 10)
        assert review1.review_text == "amazing"
        assert review1.rating == 10
        assert review1.movie == movie1
        #assert review1.timestamp == 0
        #assert repr(review1) == 0
        #time.sleep(5)
        movie2 = Movie("Harry Potter", 2010)
        review2 = Review(movie2, "amazing", 10)
        #assert review1 == review2
        #assert review2.timestamp == 0
        review3 = Review(movie2, "amazing", 50)
        assert review3.rating == None