from abc import ABC, abstractmethod
from typing import Union


class Figure(ABC):
    @property
    def name(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

    def add_area(self, figure: "Figure") -> Union[int, float]:
        if not isinstance(figure, Figure):
            raise ValueError

        return self.area + figure.area

