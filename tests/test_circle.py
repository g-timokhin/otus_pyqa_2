import pytest
import math

from src.circle import Circle


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.triangle
@pytest.mark.parametrize('radius', ['integer', 'float'])
def test_create_circle(radius, get_circle_radius):
    radius = get_circle_radius(radius=radius)
    circle = Circle(radius)
    assert circle is not None


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.triangle
@pytest.mark.parametrize('radius',
                         ['k', (-1), (-1.5)],
                         ids=['string', 'negative int', 'negative float'])
def test_create_circle_wrong_value(radius):
    with pytest.raises(ValueError):
        circle = Circle(radius)


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.square
def test_get_circle_area(get_circle_radius):
    radius = get_circle_radius(radius='integer')
    circle = Circle(radius=radius)
    test_area = circle.get_area
    target_area = round(math.pi * radius**2, 2)
    assert test_area == target_area


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.square
def test_get_circle_perimeter(get_circle_radius):
    radius = get_circle_radius(radius='integer')
    circle = Circle(radius=radius)
    test_perimeter = circle.get_perimeter
    target_perimeter = round(2 * math.pi * radius, 2)
    assert test_perimeter == target_perimeter


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.circle
def test_circle_add(get_circle_radius):
    radius = get_circle_radius(radius='integer')
    circle_1 = Circle(radius=radius)
    circle_2 = Circle(radius=radius)
    circles_sum = circle_1.add_area(circle_2)
    target_sum = 2 * round(math.pi * radius**2, 2)
    assert circles_sum == target_sum


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.circle
def test_circle_add_nonfigure(get_circle_radius):
    radius = get_circle_radius(radius='integer')
    circle = Circle(radius)
    non_figure = 'non_figure'
    with pytest.raises(ValueError):
        circle.add_area(non_figure)
