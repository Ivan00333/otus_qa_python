import math
from figure import Figure


class Triangle(Figure):

    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if not isinstance(side_a, (int, float)) or \
           not isinstance(side_b, (int, float)) or \
           not isinstance(side_c, (int, float)):
            raise ValueError("Triangle sides must be numbers")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides must be positive numbers")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Triangle with such sides does not exist")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s-self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
