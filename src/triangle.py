from .figure import Figure

import math

class Triangle(Figure):
    """class for triangle"""
    def __new__(cls, side1, side2, side3):
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            return super().__new__(cls)
        else:
            return None

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.name = "Triangle"
        self.perimeter = side1 + side2 + side3
        half_perimeter = self.perimeter / 2
        self.area = math.sqrt(half_perimeter * (half_perimeter - side1)*(half_perimeter - side2)*(half_perimeter-side3))
