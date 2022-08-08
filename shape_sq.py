from shape import Shape

class Square(Shape):
    def __init__(self, side1):
        super().__init__(4)
        self.side=side1

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4*self.side
    
    def info(self):
        super().info()
        print ("Equilateral and equilangular shape")

s=Square(4)
s.info()
print("Area: ",s.area())
print("Perimeter: ",s.perimeter())