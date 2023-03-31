import pytest
from viewing_party.movie import Movie
def test_class_movie_functionality():
    # Arrange / Act
    movie = Movie("Abc", "Horror", 5)

    # Assert
    assert isinstance(movie, Movie)
    assert movie.name == "Abc"
    assert movie.genre == "Horror"
    assert movie.rating == 5
