from typing import List

import pydantic as p


class Book(p.BaseModel):
    title: str
    author: str
    genre: str
    pages: int
    publisher: str


class User(p.BaseModel):
    name: str
    gender: str
    address: str
    age: int


class Reference(p.BaseModel):
    user: User
    books: List[Book] = p.Field(default_factory=list)

    @classmethod
    def from_user(cls, user: User) -> "Reference":
        return cls(user=user)


