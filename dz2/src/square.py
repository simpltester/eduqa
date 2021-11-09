from .rectangle import Rectangle

class Square(Rectangle):
    """class for square"""
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"
        self.area = side * side
        self.perimeter = 4 * side
