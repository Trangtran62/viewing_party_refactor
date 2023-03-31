import pytest
from viewing_party.person import Person

def test_create_person():
    # Arrange / Act
    kendall = Person("Kendall", ["Nancy"], ["Abc"], ["Pride and Prejudice"])

    # Assert
    assert isinstance(kendall, Person)

def test_person_name_is_set_correctly():
    # Arrange / Act
    nancy = Person("Nancy", ["Kendall"], ["Abc"], ["Pride and Prejudice"])
    danica = Person("Danica", ["Ping"], ["Abc"], ["Pride and Prejudice"])

    # Assert
    assert nancy.name == "Nancy"
    assert danica.name == "Danica"

def test_person_friends_list_is_set_correctly():
    # Arrange / Act
    ana = Person("Ana", ["Ariel"], ["Abc"], ["Pride and Prejudice"])

    # Assert
    assert ana.friends == ["Ariel"]

def test_friend_added_to_person():
    # Arrange
    laura = Person("Laura", ["Sage"], ["Abc"], ["Pride and Prejudice"])

    # Act
    laura.add_friend("Elizabeth")

    # Assert
    assert laura.friends == ["Sage", "Elizabeth"]

def test_no_duplicate_friends_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], ["Abc"], ["Pride and Prejudice"])

    # Act
    moyo.add_friend("Sarah")

    # Assert
    assert moyo.friends == ["Sarah"]

def test_movie_add_to_watchlist():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], ["Abc"], ["Pride and Prejudice"])

    # Act
    moyo.add_movie("Shrek")

    # Assert
    assert moyo.watchlist == ["Abc", "Shrek"]

def test_no_duplicate_movie_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], ["Abc", "Shrek"], ["Pride and Prejudice"])

    # Act
    moyo.add_movie("Shrek")

    # Assert
    assert moyo.watchlist == ["Abc", "Shrek"]


def test_movie_not_watched():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], ["Abc", "Shrek"], ["Pride and Prejudice"])

    # Act
    moyo.watched_movie("KKKK")

    # Assert
    assert moyo.watchlist == ["Abc", "Shrek"]
    assert moyo.watched == ["Pride and Prejudice", "KKKK"]

def test_movie_in_watchlist():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], ["Abc", "Shrek"], ["Pride and Prejudice"])

    # Act
    moyo.watched_movie("Abc")

    # Assert
    assert moyo.watchlist == ["Shrek"]
    assert moyo.watched == ["Pride and Prejudice", "Abc"]

