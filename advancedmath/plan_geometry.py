class Polygon:
    def __init__(self, measures):
        if type(measures) != int:
            raise TypeError("Measures must be an integer.")

        if measures < 3:
            raise ValueError("A polygon must have at least 3 measures.")
            
        self.measures = measures

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)

        if type(width) not in (int, float) or type(height) not in (int, float):
            raise TypeError("Measures must be integer or float values.")
        
        if width <= 0 or height <= 0:
            raise ValueError("Measures must have positive values.")
        
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)
