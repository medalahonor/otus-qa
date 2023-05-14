import pytest

from src.hw2.square import Square


def test_init_1():
    Square(10)


def test_init_2():
    """ __init__ не должен принимать что-то ещё, даже если это можно привести к нужному типу """
    with pytest.raises(ValueError):
        Square("5")


def test_area():
    side = 5
    square = Square(side)

    expected = pow(side, 2)
    assert square.area == expected


def test_perimeter():
    side = 10
    square = Square(side)

    expected = 4 * side
    assert square.perimeter == expected
