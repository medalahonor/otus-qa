import pytest

from src.hw2.figure import Figure


class MyFigure(Figure):
    @property
    def perimeter(self):
        return 1

    @property
    def area(self):
        return 1


@pytest.fixture
def get_figure_class():
    return MyFigure


def test_name():
    figure = MyFigure()

    assert figure.name == MyFigure.__name__


def test_add_area_1(get_figure_class):
    # пробую фикстуры, можно и без них конечно
    figure_cls = get_figure_class
    figure_1 = figure_cls()
    figure_2 = figure_cls()

    expected = figure_1.area + figure_2.area
    assert figure_1.add_area(figure_2) == expected


def test_add_area_2():
    figure_1 = MyFigure()
    not_figure = object()

    with pytest.raises(ValueError):
        figure_1.add_area(not_figure)