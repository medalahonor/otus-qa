import random

import pytest
import faker
from faker.providers import profile
from typing import List, Dict

from src.hw3.models import User, Book


def get_random_users(num: int) -> List[User]:
    fake = faker.Faker()
    fake.add_provider(profile)

    users: List[User] = []
    for _ in range(num):
        _profile = fake.profile()
        users.append(
            User(name=_profile["name"], gender=_profile["sex"], address=_profile["address"], age=random.randint(0, 75))
        )

    return users


def get_random_books(num: int) -> List[Book]:
    fake = faker.Faker()
    fake.add_provider(profile)

    books: List[Book] = []
    for _ in range(num):
        _profile = fake.profile()
        books.append(
            Book(
                title=str(hash(random.random())),
                author=_profile["name"],
                genre="",
                publisher=_profile["company"],
                pages=random.randint(50, 1000),
            )
        )

    return books



@pytest.fixture
def books_raw() -> List[List[str]]:
    return [
        ["Title", "Author", "Genre", "Pages", "Publisher"],
        ["Fundamentals of Wavelets", "Goswami, Jaideva", "signal_processing", "228", "Wiley"],
    ]


@pytest.fixture
def users_json() -> List[Dict]:
    return [{
        "_id": "5e2696e561fdc6df60d43b5f",
        "index": 0,
        "guid": "3e518b31-20f0-4dea-8de8-039af5afbd33",
        "isActive": False,
        "balance": "$3,646.47",
        "picture": "http://placehold.it/32x32",
        "age": 34,
        "eyeColor": "brown",
        "name": "Lolita Lynn",
        "gender": "female",
        "company": "HIVEDOM",
        "email": "lolitalynn@hivedom.com",
        "phone": "+1 (842) 513-2979",
        "address": "389 Neptune Avenue, Belfair, Iowa, 6116",
        "about": "Ea irure labore culpa proident sint cupidatat minim laboris labore eu exercitation aliqua duis aute. Consectetur pariatur commodo enim pariatur mollit. Laborum nisi cillum do consectetur laboris nulla id laboris eu voluptate sit consequat commodo aute. Ad minim eiusmod pariatur non cupidatat esse fugiat et laborum ullamco commodo. Sint fugiat enim elit pariatur consequat ipsum Lorem qui qui Lorem proident mollit culpa. In enim commodo culpa nostrud reprehenderit nostrud incididunt elit labore. Aute proident mollit pariatur proident enim commodo.\r\n",
        "registered": "2014-03-19T10:39:24 -06:00",
        "latitude": 0.246756,
        "longitude": -96.404056,
        "greeting": "Hello, Lolita Lynn! You have 2 unread messages.",
        "favoriteFruit": "banana"
    }]

