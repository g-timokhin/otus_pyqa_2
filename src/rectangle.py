from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a: float, side_b: float):
        try:
            if side_a <= 0 or side_b <= 0:
                raise ValueError("Side's length cannot be negative or zero")
        except TypeError:
            raise ValueError("Side's length must be a positive number")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2
