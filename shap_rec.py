from shape import Shape

class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(4)
        self.length=side1
        self.breadth=side2

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def info(self):
        super().info()
        print ("Opposite sides are equal and parallel")

r=Rectangle(4,5)
r.info()
print("Area: ",r.area())
print("Perimeter: ",r.perimeter())