from math import pi
class Shape:
    def __init__(self,n):
        self.no_of_sides=n
    def info(self):
        print("I am a 2D object with ",self.no_of_sides," side(s) ")
    def area(self):
        print ("Calculating area of shape with ",self.no_of_sides," side(s) ")
    def perimeter(self):
        print ("Calculating perimeter of shape with ",self.no_of_sides," side(s)")

class Rectangle (Shape):
    def __init__(self, side1, side2):
        super().__init__(4)
        self.length=side1
        self.breadth=side2
    def area(self):
        super().area()
        return self.length*self.breadth
    def perimeter(self):
        super().perimeter()
        return 2*(self.length+self.breadth)
    def hint(self):
        self.info()
        print("My opposite sides are equal")

class Circle (Shape):
    def __init__(self, rad):
        super().__init__(1)
        self.radius=rad
    def area(self):
        super().area()
        return pi*(self.radius**2)
    def perimeter(self):
        super().perimeter()
        return 2*pi*self.radius
    def hint(self):
        self.info()
        print("Twice a radius is its diameter.")

class Triangle (Shape):
    def __init__(self, side1, side2, side3, base, height):
        super().__init__(3)
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.base=base
        self.height=height
    def area(self):
        super().area()
        return 0.5*self.base*self.height
    def perimeter(self):
        super().perimeter()
        return self.side1+self.side2+self.side3
    def hint(self):
        self.info()
        print ("Three sided shape")
    def checktri(self):
        c1 = self.side1+self.side2
        c2 = self.side2+self.side3
        c3 = self.side1+self.side3
        if (c1<self.side3) or (c2<self.side1) or (c3<self.side2):
            return "No"
        else:
            return "Yes"

class Square(Shape):
    def __init__(self, side):
        super().__init__(4)
        self.side=side
    def area(self):
        super().area()
        return self.side**2
    def perimeter(self):
        super().perimeter()
        return self.side*4
    def hint(self):
        self.info()
        print("I am equilangular and equilateral")

r=Rectangle(2,9.9)
r.hint()
print (r.area())
print(r.perimeter())

cir=Circle(4)
print("The area : ",cir.area())
print("The perimeter: ", cir.perimeter())
cir.hint()

t = Triangle(1,2,3,3,2.5)
if t.checktri() == "Yes":
    t.hint()
    print ("The area: ",t.area())
    print ("The perimeter: ",t.perimeter())
else:
    print ("Not a triangle")

squ=Square(3)
squ.hint()
print ("Area: ",squ.area())
print ("Perimeter: ",squ.perimeter())