from plan_geometry import PI, Shape


class Prism(Shape):
    def __init__(self, area, height):
        super().__init__(2)
      
        self.validate_measure(area)
        self.validate_measure(height)

        self.area = area
        self.height = height

    def volume(self):
        return self.area * self.height


class Cobblestone(Shape):
    def __init__(self, a, b, c):
        super().__init__(6)

        self.validate_measure(a)
        self.validate_measure(b)
        self.validate_measure(c)

        self.a = a
        self.b = b
        self.c = c


class Cube(Cobblestone):
    def __init__(self, measure):
        super().__init__(measure, measure, measure)
        self.measure = measure

    def volume(self):
        return self.measure ** 3    


class Cylinder(Shape):    
    def __init__(self, radius, height):
        super().__init__(2)

        self.validate_measure(radius)
        self.validate_measure(height)

        self.radius = radius
        self.height = height

    def volume(self):
        return PI * (self.radius ** 2) * self.height


class Pyramid(Shape):
    def __init__(self, area, height):
        super().__init__(1)

        self.validate_measure(area)
        self.validate_measure(height)

        self.area = area
        self.height = height
        
    def volume(self):
        return (self.area * self.height) / 3


class Cone(Shape):
    def __init__(self, radius, height):
        super().__init__(1)

        self.validate_measure(radius)
        self.validate_measure(height)

        self.radius = radius
        self.height = height

    def volume(self):
        return (PI * (self.radius ** 2) * self.height) / 3 
