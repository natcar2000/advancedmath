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


class Diamond(Shape):
    def __init__(self, larger_diagonal, smaller_diagonal):
        super().__init__(4)

        self.validate_measure(larger_diagonal)
        self.validate_measure(smaller_diagonal)

        self.larger_diagonal = larger_diagonal
        self.smaller_diagonal = smaller_diagonal

    def area(self):
        return (self.larger_diagonal * self.smaller_diagonal) / 2


class Trapezoid(Shape):
    def __init__(self, larger_base, smaller_base, height):
        super().__init__(4)

        self.validate_measure(larger_base)
        self.validate_measure(smaller_base)
        self.validate_measure(height)

        self.larger_base = larger_base
        self.smaller_base = smaller_base
        self.height = height

    def area(self):
        return ((self.larger_base + self.smaller_base) * self.height) / 2 


class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.validate_measure(a)
        self.validate_measure(b)
        self.validate_measure(c)
        self.validate_measure(height)
        
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The measures cannot form a triangle.")
        
        super().__init__(3)

        self.a = a
        self.b = b
        self.c = c
        self.height = height
   
    def area(self):
        return(self.a * self.height) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def is_equilateral(self):
        return self.a == self.b == self.c

    def is_isosceles(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

    def is_scalene(self):
        return self.a != self.b and self.a != self.c and self.b != self.c

    def is_right(self):
        sides = sorted([self.a, self.b, self.c]) 
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


class Circle(Shape):
    def __init__(self, circumference_radius):
        super().__init__(1)

        self.validate_measure(radius)        
        self.circumference_radius = circumference_radius

    def area(self):
        return PI * (self.radius ** 2) 

    def circumference_diameter(self):
        return 2 * self.radius
    
    def circumference_length(self):
        return self.circumference_diameter() * PI
