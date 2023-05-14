import math
from typing import Union

from src.hw2.figure import Figure


class Circle(Figure):
    def __init__(self, radius: Union[int, float]):
        if type(radius) not in (int, float):
            raise ValueError
        self.radius = radius

    @property
    def area(self):
        return math.pi * pow(self.radius, 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    print(Circle().area)
