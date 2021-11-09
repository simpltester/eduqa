from src.circle import Circle
import pytest

@pytest.mark.parametrize ("radius", [1, 2, 3, 10.5, 999])
def test_create_circle(radius):
    assert Circle(radius)

@pytest.mark.parametrize ("radius", [-1, 0, "3", [10], None])
def test_create_circle_with_errors(radius):
    with pytest.raises(Exception):
        Circle(radius)

def test_check_circle_name():
    circle = Circle(1)
    assert circle.name == "Circle"

@pytest.mark.parametrize ("radius, area", [(1, 3.1), (2, 12.6), (3, 28.3)])
def test_check_circle_area(radius, area):
    circle = Circle(radius)
    assert round(circle.area, 1) == area

@pytest.mark.parametrize ("side, perimeter", [(1, 6.3), (2, 12.6), (3, 18.8)])
def test_check_circle_perimeter(side,perimeter):
    circle = Circle(side)
    assert round(circle.perimeter, 1) == perimeter

def test_circle_add_area():
    circle1 = Circle(1)
    circle2 = Circle(1)
    add_result = circle1.add_area(circle2)
    assert add_result == circle1.area + circle2.area

def test_circle_add_area_with_errors():
    with pytest.raises(Exception):
        circle = Circle(3)
        circle.add_area(1)
