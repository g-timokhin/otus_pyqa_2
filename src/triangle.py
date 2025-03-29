from src.figure import Figure
import src.trigonometry as tr


class Triangle(Figure):

    def __init__(self, side_a: float, side_b: float, side_c: float):
        try:
            if side_a <= 0 or side_b <= 0:
                raise ValueError("Side's length cannot be negative or zero")
            elif not tr.inequality(side_a, side_b, side_c):
                raise ValueError("Sides' lengths must satisfy strong triangle inequality")
        except TypeError:
            raise ValueError("Side's length must be a positive number")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        return tr.tri_area(self.side_a, self.side_b, self.side_c)

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
