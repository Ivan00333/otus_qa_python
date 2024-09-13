import pytest
from src.circle import Circle
from src.square import Square


@pytest.mark.usefixtures("login")
class TestCircle():

    @pytest.mark.parametrize("radius, expected_area", [
        (5, 78.53981633974483),
        (2.5, 19.634954084936208)
    ])
    def test_circle_area(self, radius, expected_area):
        circle = Circle(radius=radius)
        circle_area = circle.get_area
        assert circle_area == expected_area, \
            f"Площадь окружности должна быть равна {expected_area}, расчетная площадь {circle_area}"

    @pytest.mark.parametrize("radius, expected_perimeter", [
        (5, 31.41592653589793),
        (2.5, 15.707963267948966)
    ])
    def test_circle_perimeter(self, radius, expected_perimeter):
        circle = Circle(radius=radius)
        circle_perimeter = circle.get_perimeter
        assert circle_perimeter == expected_perimeter, \
            f"Периметр окружности должен быть равен {expected_perimeter}, расчетный периметр {circle_perimeter}"

    def test_circle_add_area(self):
        circle = Circle(7)
        square = Square(10)
        area_sum = circle.add_area(square)
        assert area_sum == 253.93804002589985, \
            f"Сумма площадей фигур должна быть {253.93804002589985}, рассчетная сумма {area_sum}"

    @pytest.mark.parametrize("radius", [0, -2, -3.45])
    def test_negative_radius_less_than_0(self, radius):
        with pytest.raises(ValueError, match="Circle radius can't be less than 0"):
            Circle(radius=radius)

    def test_negative_radius_not_number(self):
        with pytest.raises(ValueError, match="Square side must be number"):
            Circle("3")
