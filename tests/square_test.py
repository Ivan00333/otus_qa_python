import pytest
from src.square import Square

@pytest.mark.usefixtures("login")
class TestSquare():

    @pytest.mark.parametrize("side_a, expected_area", [
        (5, 25),
        (2.5, 6.25)
    ])
    def test_square_area(self, side_a, expected_area):
        square = Square(side_a)
        square_area = square.get_area
        assert square_area == expected_area,\
            f"Площадь квадрата должна быть равна {expected_area}, расчетная площадь {square_area}"

    @pytest.mark.parametrize("side_a, expected_perimeter", [
        (5, 20),
        (2.5, 10)
    ])
    def test_square_perimeter(self, side_a, expected_perimeter):
        square = Square(side_a)
        square_perimeter = square.get_perimeter
        assert square_perimeter == expected_perimeter,\
            f"Периметр прямоугольника должен быть равен {expected_perimeter}, расчетный периметр {square_perimeter}"


    @pytest.mark.parametrize("side_a", [0, -2])
    def test_negative_side_less_than_0(self, side_a):
        with pytest.raises(ValueError, match="Square side can't be less than 0"):
            Square(side_a)

    def test_negative_side_not_number(self):
        with pytest.raises(ValueError, match="Square side must be numbers"):
            Square("3")
