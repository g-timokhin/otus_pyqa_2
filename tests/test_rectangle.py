import pytest

from src.rectangle import Rectangle


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.rectangle
@pytest.mark.parametrize('sides',
                         ['integer',
                          'float'])
def test_create_rectangle(get_rectangle_sides, sides):
    side_a, side_b = get_rectangle_sides(sides=sides)
    rectangle = Rectangle(side_a, side_b)
    assert rectangle is not None


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.rectangle
@pytest.mark.parametrize('side_a, side_b',
                         [('kk', 'll'),
                          (-1, -2),
                          (-1.5, -2.5)],
                         ids=['string',
                              'negative int',
                              'negative float'])
def test_create_rectangle_wrong_value(side_a, side_b):
    try:
        square = Rectangle(side_a, side_b)
    except ValueError:
        pass


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.rectangle
def test_get_rectangle_area(get_rectangle_sides):
    side_a, side_b = get_rectangle_sides(sides='integer')
    rectangle = Rectangle(side_a, side_b)
    test_area = rectangle.get_area
    target_area = side_a * side_b
    assert test_area == target_area


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.rectangle
def test_get_rectangle_perimeter(get_rectangle_sides):
    side_a, side_b = get_rectangle_sides(sides='integer')
    rectangle = Rectangle(side_a, side_b)
    test_perimeter = rectangle.get_perimeter
    target_perimeter = side_a * 2 + side_b * 2
    assert test_perimeter == target_perimeter


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.rectangle
def test_rectangle_add(get_rectangle_sides):
    side_a, side_b = get_rectangle_sides(sides='integer')
    rectangle_1 = Rectangle(side_a, side_b)
    rectangle_2 = Rectangle(side_a, side_b)
    rectangles_sum = rectangle_1.add_area(rectangle_2)
    target_sum = 2 * (side_a * side_b)
    assert rectangles_sum == target_sum


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.rectangle
def test_rectangle_add_nonfigure(get_rectangle_sides):
    side_a, side_b = get_rectangle_sides(sides='integer')
    rectangle = Rectangle(side_a, side_b)
    non_figure = 'non_figure'
    try:
        rectangle.add_area(non_figure)
    except ValueError:
        pass
