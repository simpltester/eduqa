class Figure:

    def __init__(self):
        self.name = "Figure"
        self.area = None
        self.perimeter = None
    
    def add_area(self, area):
        if isinstance(area, Figure):
            sum_area = self.area + area.area
            return sum_area
        else:
            raise ValueError ("take wrong class")
