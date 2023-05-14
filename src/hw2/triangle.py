from typing import Union
from math import sqrt

from src.hw2.figure import Figure


class Triangle(Figure):
    def __init__(
            self,
            a: Union[int, float],
            b: Union[int, float],
            c: Union[int, float],
    ):
        is_allowed_type = lambda x: type(x) in (int, float)
        if not is_allowed_type(a) or not is_allowed_type(b) or not is_allowed_type(c):
            raise ValueError(f"A Triangle sides must be str or int, actual a={type(a)}, b={type(b)}, c={type(c)}")

        is_triangle_exists = lambda a, b, c: a + b >= c and b + c >= a and c + a >= b
        if not is_triangle_exists(a, b, c):
            raise ValueError(f"There's no triangle with the specified sides: a={a!r}, b={b!r}, c={c!r}")

        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self) -> Union[int, float]:
        s = (self.a + self.b + self.c) / 2
        area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    @property
    def perimeter(self) -> Union[int, float]:
        return self.a + self.b + self.c
