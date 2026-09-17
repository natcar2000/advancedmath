from plan_geometry import Shape


class Prism(Shape):
    def __init__(self, area, height):
        super().__init__(0)
      
        self.validate_measure(area)
        self.validate_measure(height)

        self.area = area
        self.height = height

    def volume(self):
        return self.area * self.height


class Cobblestone(Shape):
    def __init__(self, a, b, c):
        super().__init__(0)

        self.validate_measure(a)
        self.validate_measure(b)
        self.validate_measure(c)

        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c


class Cube(Cobblestone):
    def __init__(self, measure):
        super().__init__(measure, measure, measure)
        self.measure = measure

    def volume(self):
        return self.measure ** 3    
