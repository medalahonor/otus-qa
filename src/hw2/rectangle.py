from typing import Union

from src.hw2.figure import Figure


class Rectangle(Figure):
    def __init__(self, length: Union[int, float], width: Union[int, float]):
        is_allowed_type = lambda x: type(x) in (int, float)
        if not is_allowed_type(length) or not is_allowed_type(width):
            raise ValueError

        self.length = length
        self.width = width

    @property
    def area(self) -> Union[int, float]:
        return self.length * self.width

    @property
    def perimeter(self) -> Union[int, float]:
        return 2 * (self.length + self.width)