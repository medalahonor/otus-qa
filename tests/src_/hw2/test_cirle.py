import pytest
import math

from src.hw2.circle import Circle


def test_init_1():
    radius = 10
    circle = Circle(radius)
    assert circle.radius == radius


def test_init_2():
    """ __init__ не должен принимать что-то ещё, даже если это можно привести к нужному типу """
    radius = "10.5"
    with pytest.raises(ValueError):
        circle = Circle(radius)


def test_area():
    radius = 5
    circle = Circle(radius)

    expected = math.pi * pow(radius, 2)
    assert circle.area == expected


def test_perimeter():
    radius = 5
    circle = Circle(radius)

    expected = 2 * math.pi * radius
    assert circle.perimeter == expected



