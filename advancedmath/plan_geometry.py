PI = 3.141592653589793

class Shape:
    def __init__(self, measures):
        self.validate_measure(measures)
        self.measures = measures

    @staticmethod
    def validate_measure(value):
        if type(value) not in (int, float):
            raise TypeError("Measure must have an integer or float value.")

        if value <= 0:
            raise ValueError("Measure must have a positive value.")

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(4)

        self.validate_measure(width)
        self.validate_measure(height)
        
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Parallelogram(Shape):
    def __init__(self, base, height):
        super().__init__(4)
        
        self.validate_measure(base)
        self.validate_measure(height)
        
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class Circumference(Shape):
    def __init__(self, radius):
        super().__init__(1)

        self.validate_measure(radius)        
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2) 

    def diameter(self):
        return 2 * self.radius
    
    def circumference_length(self):
        return self.diameter() * PI
