from src.figure import Figure
import math


class Circle(Figure):

    def __init__(self, radius: float):
        try:
            if radius <= 0:
                raise ValueError("Radius cannot be negative or zero")
        except TypeError:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    @property
    def get_area(self):
        return round(math.pi*self.radius**2, 2)

    @property
    def get_perimeter(self):
        return round(math.pi*self.radius*2, 2)
