from .figure import Figure

import math

class Circle(Figure):
    """ class for circle"""
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.perimeter = 2* math.pi * radius
        self.area = math.pi * (radius ** 2)