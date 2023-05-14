from typing import Union

from src.hw2.figure import Figure


class Square(Figure):
    def __init__(self, side: Union[int, float]):
        if type(side) not in (int, float):
            raise ValueError(f"`side` must be int or float, actual {type(side).__name__}")

        self.side = side

    @property
    def area(self) -> Union[int, float]:
        return pow(self.side, 2)

    @property
    def perimeter(self) -> Union[int, float]:
        return 4 * self.side
