import csv
import json
from typing import List, Dict, Sequence, Generator

from src.hw3.models import Book, User, Reference


def get_csv_data(filepath: str) -> List[List[str]]:
    with open(filepath, newline="") as file:
        reader = csv.reader(file)
        return [l for l in reader]


def get_json_data(filepath: str) -> List[Dict]:
    with open(filepath) as file:
        return json.load(file)


def get_books(books_raw: List[list[str]]) -> List[Book]:
    books_head = books_raw[0]
    books_data = books_raw[1:]

    book_keys = [key.lower() for key in books_head]

    _books = []
    for book_data in books_data:
        kwargs = dict(zip(book_keys, book_data))
        _books.append(Book(**kwargs))

    return _books


def get_users(users_json: List[Dict]) -> List[User]:
    return [User(**item) for item in users_json]


def get_cycled_sequence(sequence: Sequence) -> Generator:
    if len(sequence) == 0:
        raise ValueError("sequence must be non-empty")

    # Если переместить yield в тело функции, то при вызове будет возвращаться генератор без проверки на длину
    def func():
        while True:
            for item in sequence:
                yield item

    return func()


def distribute_books(users: List[User], books: List[Book]) -> List[Reference]:
    references = [Reference.from_user(user) for user in users]
    references_cycled = get_cycled_sequence(references)

    for reference, book in zip(references_cycled, books):
        reference.books.append(book)

    return references


def get_json_results(references: List[Reference]) -> List[Dict]:
    return [
        dict(books=[b.dict() for b in reference.books], **reference.user.dict())
        for reference in references
    ]


if __name__ == '__main__':
    books_filepath = "resources/books.csv"
    users_filepath = "resources/users.json"
    results_filepath = "resources/results.json"

    books_raw = get_csv_data(books_filepath)
    books = get_books(books_raw)

    users_json = get_json_data(users_filepath)
    users = get_users(users_json)

    references = distribute_books(users, books)
    references_json = get_json_results(references)

    with open(results_filepath, "w") as file:
        json.dump(references_json, file)
