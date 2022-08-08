from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,n):
        self.no_of_sides=n

    def info(self):
        print("I am a 2 dimensional object with ", self.no_of_sides, " sides.")

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass