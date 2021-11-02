from .figure import Figure

class Square(Figure):
    """class for square"""
    def __init__(self, side):
        super().__init__()
        self.name = "Square"
        self.area = side * side
        self.perimeter = 4 * side