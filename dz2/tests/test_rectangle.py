from src.rectangle import Rectangle
import pytest

@pytest.mark.parametrize ("side1, side2", [(1, 1), (2, 4), (3.5, 6), (4, 8)])
def test_create_rectangle(side1, side2):
    assert Rectangle(side1, side2)

@pytest.mark.parametrize ("side1, side2", [(-1, 2), (1, 0), ("2", 4), ([3.5], 4), (None, 3)])
def test_create_rectangle_with_errors(side1, side2):
    with pytest.raises(Exception):
        Rectangle(side1, side2)

def test_check_rectangle_name():
    rect = Rectangle(1, 2)
    assert rect.name == "Rectangle"

@pytest.mark.parametrize ("sides, area", [((1, 2), 2), ((2, 3), 6), ((3, 4), 12), ((4, 5), 20)])
def test_check_rectangle_area(sides, area):
    rect = Rectangle(*sides)
    assert rect.area == area

@pytest.mark.parametrize ("sides, perimeter", [((1, 2), 6), ((2, 3), 10), ((3, 4), 14), ((4, 5), 18)])
def test_check_rectangle_perimeter(sides,perimeter):
    rect = Rectangle(*sides)
    assert rect.perimeter == perimeter

@pytest.mark.parametrize ("sides, area_sum", [((1, 2), 4), ((2, 3), 8), ((3, 4), 14), ((4, 5), 22)])
def test_rectangle_add_area(sides, area_sum):
    rectangle1 = Rectangle(*sides)
    rectangle2 = Rectangle(1, 2)
    add_result = rectangle1.add_area(rectangle2)
    assert add_result == area_sum

def test_rectangle_add_area_with_errors():
    with pytest.raises(Exception):
        rect = Rectangle(1, 2)
        rect.add_area(1)
