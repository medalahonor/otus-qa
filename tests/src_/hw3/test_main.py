import pytest

from src.hw3.main import get_books, get_users, get_cycled_sequence, distribute_books
from src.hw3.models import Book, User
from tests.src_.hw3.conftest import get_random_users, get_random_books


def test_get_books(books_raw):
    expected = [Book(
        title="Fundamentals of Wavelets",
        author="Goswami, Jaideva",
        genre="signal_processing",
        pages="228",
        publisher="Wiley",
    )]
    actual = get_books(books_raw)

    assert expected == actual


def test_get_users(users_json):
    expected = [
        User(name="Lolita Lynn", gender="female", address="389 Neptune Avenue, Belfair, Iowa, 6116", age=34),
    ]
    actual = get_users(users_json)

    assert expected == actual


def test_get_cycled_sequence_1():
    with pytest.raises(ValueError):
        get_cycled_sequence([])


def test_get_cycled_sequence_2():
    seq = [1]
    cycled_seq = get_cycled_sequence(seq)

    expected = seq*5
    actual = [next(cycled_seq) for _ in range(5)]

    assert expected == actual


@pytest.mark.parametrize(
    ["users_num", "books_num", "expected_distribution"],
    [
        [3, 10, [4, 3, 3]],
        [5, 4, [1, 1, 1, 1, 0]],
    ]
)
def test_distribute_books(users_num, books_num, expected_distribution):
    users = get_random_users(users_num)
    books = get_random_books(books_num)

    references = distribute_books(users, books)

    actual_distribution = [len(ref.books) for ref in references]
    assert expected_distribution == actual_distribution
