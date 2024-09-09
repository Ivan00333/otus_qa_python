from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: int | float):
        if not isinstance(side_a, (int, float)):
            raise ValueError("Square side must be numbers")
        if side_a <= 0:
            raise ValueError("Square side can't be less than 0")
        super().__init__(side_a, side_a)
