from math import pi
from Shape import shape
class Circle(shape):
    PI = 3.14
    def __init__(self, radius): 
        self.radius = radius
    
    def calculate_area(self):
        self.area = pi *self.radius *self.radius
        return self.area
    
    
    def calculate_perimeter(self):
        self.perimeter = 2 * pi * self.radius
        return self.perimeter

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
