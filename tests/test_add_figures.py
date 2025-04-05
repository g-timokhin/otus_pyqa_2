import pytest
import math

from src.triangle import Triangle
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.trigonometry import tri_area


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.parametrize('figures',
                         ['circle&rectangle',
                          'circle&square',
                          'circle&triangle',
                          'rectangle&square',
                          'rectangle&triangle',
                          'square&triangle'])
def test_add_figures(figures):
    match figures:
        case 'circle&rectangle':
            radius = 3
            circle = Circle(radius=radius)
            circle_area = round(math.pi * radius ** 2, 2)
            side_a, side_b = 3, 4
            rectangle = Rectangle(side_a, side_b)
            rectangle_area = side_a * side_b
            assert circle.add_area(rectangle) == circle_area + rectangle_area
        case 'circle&square':
            radius = 3
            circle = Circle(radius=radius)
            circle_area = round(math.pi * radius ** 2, 2)
            side = 3
            square = Square(side=side)
            square_area = side ** 2
            assert circle.add_area(square) == circle_area + square_area
        case 'circle&triangle':
            radius = 3
            circle = Circle(radius=radius)
            circle_area = round(math.pi * radius ** 2, 2)
            side_a, side_b, side_c = 3, 4, 5
            triangle = Triangle(side_a=side_a,
                                side_b=side_b,
                                side_c=side_c)
            triangle_area = tri_area(side_a=side_a,
                                     side_b=side_b,
                                     side_c=side_c)
            assert triangle.add_area(circle) == circle_area + triangle_area
        case 'rectangle&square':
            side_a, side_b = 3, 4
            rectangle = Rectangle(side_a, side_b)
            rectangle_area = side_a * side_b
            side = 3
            square = Square(side=side)
            square_area = side ** 2
            assert rectangle.add_area(square) == rectangle_area + square_area
        case 'rectangle&triangle':
            side_a, side_b = 3, 4
            rectangle = Rectangle(side_a, side_b)
            rectangle_area = side_a * side_b
            side_a, side_b, side_c = 3, 4, 5
            triangle = Triangle(side_a=side_a,
                                side_b=side_b,
                                side_c=side_c)
            triangle_area = tri_area(side_a=side_a,
                                     side_b=side_b,
                                     side_c=side_c)
            assert rectangle.add_area(triangle) == rectangle_area + triangle_area
        case 'square&triangle':
            side = 3
            square = Square(side=side)
            square_area = side ** 2
            side_a, side_b, side_c = 3, 4, 5
            triangle = Triangle(side_a=side_a,
                                side_b=side_b,
                                side_c=side_c)
            triangle_area = tri_area(side_a=side_a,
                                     side_b=side_b,
                                     side_c=side_c)
            assert square.add_area(triangle) == square_area + triangle_area
