class Parent1:
    def __init__(self):
        self.p1inputn=input("Enter name of Parent 1: ")
        self.p1inputa=int(input("Enter age of Parent 1: "))
        self.p1inputg=input("Enter gender of Parent 1: ")
        print("Parent Class 1")
    def printp1(self):
        print ("Name: ",self.p1inputn)
        print ("Age: ",self.p1inputa)
        print ("Gender: ",self.p1inputg)

class Parent2:
    def __init__(self):
        self.p2inputn=input("Enter name of Parent 2: ")
        self.p2inputa=int(input("Enter age of Parent 2: "))
        self.p2inputg=input("Enter gender of Parent 2: ")
        print("Parent Class 2")

    def printp2 (self):
        print ("Name: ",self.p2inputn)
        print ("Age: ", self.p2inputa)
        print ("Gender: ",self.p2inputg)

class Child1(Parent1, Parent2):
    def __init__(self):
        Parent2.__init__(self)
        Parent1.__init__(self)
        self.cinputn=input("Enter name of Child 1: ")
        self.cinputa=int(input("Enter age of Child 1: "))
        self.cinputg=input("Enter gender of Child 1: ")
        print("Derived Class")

    def printnames (self):
        print("Parent 1 Details: ")
        Parent1.printp1(self)
        print("Parent 2 Details: ")
        Parent2.printp2(self)
        print("Child Details: ")
        print ("Name: ",self.cinputn)
        print ("Age: ",self.cinputa)
        print ("Gender: ",self.cinputg)

ob=Child1()
ob.printnames()