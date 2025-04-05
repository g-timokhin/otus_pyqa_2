import pytest


@pytest.fixture(scope='module')
def get_rectangle_sides():
    def _wrapper(sides: str):
        if sides == 'integer':
            return 3, 5
        elif sides == 'float':
            return 3.5, 5.5
        else:
            return ValueError("Should be 'integer' or 'float'")
    yield _wrapper


@pytest.fixture(scope='module')
def get_square_side():
    def _wrapper(side: str):
        if side == 'integer':
            return 3
        elif side == 'float':
            return 3.5
        else:
            return ValueError("Should be 'integer' or 'float'")
    yield _wrapper


@pytest.fixture(scope='module')
def get_triangle_sides():
    def _wrapper(sides: str):
        if sides == 'integer':
            return 3, 4, 5
        elif sides == 'float':
            return 3.5, 4.5, 5.5
        else:
            return ValueError("Should be 'integer' or 'float'")
    yield _wrapper


@pytest.fixture(scope='module')
def get_circle_radius():
    def _wrapper(radius: str):
        if radius == 'integer':
            return 3
        elif radius == 'float':
            return 3.5
        else:
            return ValueError("Should be 'integer' or 'float'")
    yield _wrapper


