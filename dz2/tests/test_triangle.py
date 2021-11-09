from src.triangle import Triangle
import pytest

VALID_SIDES = [(7, 3, 5), (3.5, 6, 8), (4, 8, 9)]
BAD_VALID_SIDES = [(2, 3, 5), (1, 6, 8), (3, 4, 9)]
INVALID_SIDES = [(-7, 3, 5), (1, 0, 8), (9, 6, "2"), (7, None, 5)]
EXPECTED_AREA = (6.5, 9.7, 16.0)
EXPECTED_PERIMETER = (15, 17.5, 21)

@pytest.mark.parametrize ("sides", VALID_SIDES)
def test_create_triangle(sides):
    assert Triangle(*sides)

@pytest.mark.parametrize ("sides", BAD_VALID_SIDES)
def test_create_bad_triangle(sides):
    assert Triangle(*sides) == None

@pytest.mark.parametrize ("sides", INVALID_SIDES)
def test_create_triangle_with_errors(sides):
    with pytest.raises(Exception):
        Triangle(*sides)

def test_check_triangle_name():
    triangle = Triangle(7, 3, 5)
    assert triangle.name == "Triangle"

@pytest.mark.parametrize ("sides, area", zip(VALID_SIDES, EXPECTED_AREA))
def test_check_triangle_area(sides, area):
    triangle = Triangle(*sides)
    assert round(triangle.area, 1) == area

@pytest.mark.parametrize ("sides, perimeter", zip(VALID_SIDES, EXPECTED_PERIMETER))
def test_check_triangle_perimeter(sides, perimeter):
    triangle = Triangle(*sides)
    assert triangle.perimeter == perimeter

def test_triangle_add_area():
    triangle1 = Triangle(7, 3, 5)
    triangle2 = Triangle(3, 3, 3)
    add_result = triangle1.add_area(triangle2)
    assert add_result == triangle1.area + triangle2.area

def test_triangle_add_area_with_errors():
    with pytest.raises(Exception):
        triangle = Triangle(3, 3, 3)
        triangle.add_area(1)
