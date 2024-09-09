import math
from figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        if not isinstance(radius, (float, int)):
            raise ValueError("Square side must be number")
        if radius <= 0:
            raise ValueError("Circle radius can't be less than 0")

        self.radius = radius

    @property
    def get_area(self):
        return math.pi * self.radius ** 2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.radius
