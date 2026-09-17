class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.widht = widht
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)
