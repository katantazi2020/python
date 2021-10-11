class Rectangle():
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calculate_area(self):
        self.rectarea = self.height * self.width
        return self.rectarea
    
    def calculate_perimeter(self):
        self.perimeter = 2*(self.height + self.width)
        return self.perimeter


rect = Rectangle(10, 20)
print(rect.calculate_area())
print(rect.calculate_perimeter())
