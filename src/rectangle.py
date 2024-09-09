from figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a: int | float, side_b: int | float):
        if not isinstance(side_a, (int, float)) or not isinstance(side_b, (int, float)):
            raise ValueError("Rectangle sides must be numbers")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides can't be less than 0")

        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2
