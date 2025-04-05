import pytest

from src.triangle import Triangle
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.parametrize('figure_1, figure_2',
                         [
                             (Circle(3), Rectangle(3, 4)),
                             (Circle(3), Square(3)),
                             (Circle(3), Triangle(3, 4, 5)),
                             (Rectangle(3, 4), Square(3)),
                             (Rectangle(3, 4), Triangle(3, 4, 5)),
                             (Square(3), Triangle(3, 4, 5))
                         ],
                         ids=[
                                'Circle and Rectangle',
                                'Circle and Square',
                                'Circle and Triangle',
                                'Rectangle and Square',
                                'Rectangle and Triangle',
                                'Square and Triangle'
                             ]
                         )
def test_add_figures(figure_1, figure_2):
    assert figure_1.add_area(figure_2) == figure_1.get_area + figure_2.get_area
