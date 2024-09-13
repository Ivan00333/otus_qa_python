import pytest
from src.triangle import Triangle


@pytest.mark.usefixtures("login")
class TestTriangle():

    @pytest.mark.parametrize("side_a, side_b, side_c, expected_area", [
        (5, 4, 7, 9.797958971132712),
        (2.5, 3.5, 3, 3.6742346141747673)
    ])
    def test_triangle_area(self, side_a, side_b, side_c, expected_area):
        triangle = Triangle(side_a, side_b, side_c)
        triangle_area = triangle.get_area
        assert triangle_area == expected_area, \
            f"Площадь треугольника должна быть равна {expected_area}, расчетная площадь {triangle_area}"

    @pytest.mark.parametrize("side_a, side_b, side_c, expected_perimeter", [
        (5, 4, 2, 11),
        (2.5, 3.5, 3, 9)
    ])
    def test_triangle_perimeter(self, side_a, side_b, side_c, expected_perimeter):
        triangle = Triangle(side_a, side_b, side_c,)
        triangle_perimeter = triangle.get_perimeter
        assert triangle_perimeter == expected_perimeter, \
            f"Периметр треугольника должен быть равен {expected_perimeter}, расчетный периметр {triangle_perimeter}"

    def test_negative_such_sides(self):
        with pytest.raises(ValueError, match="Triangle with such sides does not exist"):
            Triangle(4, 10, 25)
