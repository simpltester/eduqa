from .figure import Figure

class Rectangle(Figure):
    """class for rectangle"""
    def __init__(self, side1, side2):
        super().__init__()
        self.name = "Rectangle"
        self.area = side1 * side2
        self.perimeter = 2 * (side1 + side2)
