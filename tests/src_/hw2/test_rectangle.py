import pytest

from src.hw2.rectangle import Rectangle


def test_init_1():
    a, b = 1, 2.5
    Rectangle(a, b)


def test_init_2():
    """ __init__ не должен принимать что-то ещё, даже если это можно привести к нужному типу """
    a, b = 1, "5"
    with pytest.raises(ValueError):
        Rectangle(a, b)


def test_area():
    length, width = 5, 2
    rectangle = Rectangle(length, width)

    expected = length * width
    assert rectangle.area == expected


def test_perimeter():
    length, width = 5, 2
    rectangle = Rectangle(length, width)

    expected = 2 * (length + width)
    assert rectangle.perimeter == expected
