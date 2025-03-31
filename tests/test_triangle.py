import pytest

from src.triangle import Triangle
from src.trigonometry import tri_area


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.triangle
@pytest.mark.parametrize('sides',
                    ['integer',
                     'float'])
def test_create_triangle(get_triangle_sides, sides):
    side_a, side_b, side_c = get_triangle_sides(sides=sides)
    triangle = Triangle(side_a=side_a,
                        side_b=side_b,
                        side_c=side_c)
    assert triangle is not None


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.triangle
@pytest.mark.parametrize('side_a, side_b, side_c',
                         [('jk', 'jk', 'kl'),
                          (-3, -4, -5),
                          (-3.5, -4.5, -5.5)],
                         ids=['strings',
                              'negative ints',
                              'negative floats'])
def test_create_triangle_wrong_value(side_a, side_b, side_c):
    try:
        triangle = Triangle(side_a, side_b, side_c)
    except ValueError:
        pass


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.triangle
@pytest.mark.parametrize('side_a, side_b, side_c',
                         [(1, 2, 3), (1.1, 2.1, 3.1)],
                         ids=['int sides', 'float sides'])
def test_create_impossible_triangle(side_a, side_b, side_c):
    try:
        triangle = Triangle(side_a, side_b, side_c)
    except ValueError:
        pass


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.triangle
def test_get_triangle_area(get_triangle_sides):
    side_a, side_b, side_c = get_triangle_sides(sides='integer')
    triangle = Triangle(side_a, side_b, side_c)
    test_area = triangle.get_area
    target_area = tri_area(side_a, side_b, side_c)
    assert test_area == target_area


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.triangle
def test_get_triangle_perimeter(get_triangle_sides):
    side_a, side_b, side_c = get_triangle_sides(sides='integer')
    triangle = Triangle(side_a, side_b, side_c)
    test_perimeter = triangle.get_perimeter
    target_perimeter = side_a + side_b + side_c
    assert test_perimeter == target_perimeter


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.triangle
def test_triangle_add(get_triangle_sides):
    side_a, side_b, side_c = get_triangle_sides(sides='integer')
    triangle_1 = Triangle(side_a, side_b, side_c)
    triangle_2 = Triangle(side_a, side_b, side_c)
    assert triangle_1.add_area(triangle_2) == 2*tri_area(side_a, side_b, side_c)


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_add_nonfigure(get_triangle_sides):
    side_a, side_b, side_c = get_triangle_sides(sides='integer')
    triangle = Triangle(side_a, side_b, side_c)
    non_figure = 'non_figure'
    try:
        triangle.add_area(non_figure)
    except ValueError:
        pass
