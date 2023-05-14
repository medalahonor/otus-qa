import pytest


from src.hw2.triangle import Triangle


def test_init_1():
    Triangle(2, 3, 4)


def test_init_2():
    """ __init__ не должен принимать что-то ещё, даже если это можно привести к нужному типу """
    with pytest.raises(ValueError):
        Triangle(1, 2, "5")


@pytest.mark.parametrize(
    ["a", "b", "c"],
    [
        [1, 1, 10],
        [1, 10, 1],
        [10, 1, 1],
    ]
)
def test_init_3(a, b, c):
    """ Треугольник с указанными сторонами должен существовать """
    a, b, c = 1, 1, 10
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_area():
    a, b, c = 5, 12, 13
    triangle = Triangle(a, b, c)

    expected = 30
    assert triangle.area == expected


def test_perimeter():
    a, b, c = 5, 12, 13
    triangle = Triangle(a, b, c)

    expected = 30
    assert triangle.perimeter == expected
