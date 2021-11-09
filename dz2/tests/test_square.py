from src.square import Square
import pytest

@pytest.mark.parametrize ("side", [1, 2, 3, 10.5, 999])
def test_create_square(side):
    assert Square(side)

@pytest.mark.parametrize ("side", [-1, 0, "3", [10], None])
def test_create_square_with_errors(side):
    with pytest.raises(Exception):
        Square(side)

def test_check_square_name():
    square = Square(1)
    assert square.name == "Square"

@pytest.mark.parametrize ("side, area", [(1, 1), (2, 4), (3, 9), (4, 16)])
def test_check_square_area(side, area):
    square = Square(side)
    assert square.area == area

@pytest.mark.parametrize ("side, perimeter", [(1, 4), (2, 8), (3, 12), (4, 16)])
def test_check_square_perimeter(side,perimeter):
    square = Square(side)
    assert square.perimeter == perimeter

@pytest.mark.parametrize ("side, area_sum", [(1, 2), (2, 5), (3, 10), (4, 17)])
def test_square_add_area(side, area_sum):
    square1 = Square(side)
    square2 = Square(1)
    add_result = square1.add_area(square2)
    assert add_result == area_sum

def test_square_add_area_with_errors():
    with pytest.raises(Exception):
        square = Square(3)
        square.add_area(1)
