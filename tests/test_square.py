import pytest

from src.square import Square


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.square
@pytest.mark.parametrize('side',
                         ['integer',
                          'float'])
def test_create_square(get_square_side, side):
    side = get_square_side(side=side)
    square = Square(side=side)
    assert square is not None


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.square
@pytest.mark.parametrize('side',
                         ['kk',
                          (-1),
                          (-1.5)],
                         ids=['string',
                              'negative int',
                              'negative float'])
def test_create_square_wrong_value(side):
    with pytest.raises(ValueError):
        square = Square(side)


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.square
def test_get_square_area(get_square_side):
    side = get_square_side(side='integer')
    square = Square(side=side)
    test_area = square.get_area
    target_area = side ** 2
    assert test_area == target_area


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.square
def test_get_square_perimeter(get_square_side):
    side = get_square_side(side='integer')
    square = Square(side=side)
    test_perimeter = square.get_perimeter
    target_perimeter = side * 4
    assert test_perimeter == target_perimeter


@pytest.mark.regress
@pytest.mark.positive
@pytest.mark.square
def test_square_add(get_square_side):
    side = get_square_side(side='integer')
    square_1 = Square(side=side)
    square_2 = Square(side=side)
    squares_sum = square_1.add_area(square_2)
    target_sum = 2 * side ** 2
    assert squares_sum == target_sum


@pytest.mark.regress
@pytest.mark.negative
@pytest.mark.square
def test_square_add_nonfigure(get_square_side):
    side = get_square_side(side='integer')
    square = Square(side=side)
    non_figure = 'non_figure'
    with pytest.raises(ValueError):
        square.add_area(non_figure)

