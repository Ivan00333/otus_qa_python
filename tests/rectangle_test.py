import pytest
from src.rectangle import Rectangle

@pytest.mark.usefixtures("login")
class TestRectangle():

    @pytest.mark.parametrize("side_a, side_b, expected_area", [
        (5, 4, 20),
        (2.5, 3.5, 8.75)
    ])
    def test_rectangle_area(self, side_a, side_b, expected_area):
        rectangle = Rectangle(side_a, side_b)
        rectangle_area = rectangle.get_area
        assert rectangle_area == expected_area,\
            f"Площадь прямоугольника должна быть равна {expected_area}, расчетная площадь {rectangle_area}"

    @pytest.mark.parametrize("side_a, side_b, expected_perimeter", [
        (5, 4, 18),
        (2.5, 3.5, 12)
    ])
    def test_rectangle_perimeter(self, side_a, side_b, expected_perimeter):
        rectangle = Rectangle(side_a, side_b)
        rectangle_perimeter = rectangle.get_perimeter
        assert rectangle_perimeter == expected_perimeter,\
            f"Периметр прямоугольника должен быть равен {expected_perimeter}, расчетный периметр {rectangle_perimeter}"


    @pytest.mark.parametrize("side_a, side_b",
        [
            (0, -2),
            (-3, 0),
            (0, 0),
            (-2, -4),
            (4, -3)
        ])
    def test_negative_sides_less_than_0(self, side_a, side_b):
        with pytest.raises(ValueError, match="Rectangle sides can't be less than 0"):
            Rectangle(side_a, side_b)

    def test_negative_side_not_number(self):
        with pytest.raises(ValueError, match="Rectangle sides must be numbers"):
            Rectangle("3", 4)
