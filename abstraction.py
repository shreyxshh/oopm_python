'''
we cant directly implement abstraction in python 
to achieve this we use library called 'abc'
'''
from abc import ABC, abstractmethod
class shapes(ABC):

    @abstractmethod #decorator 
    def perimeter():
        pass

    @abstractmethod
    def area():
        pass
'''all these methods which are being created in the parent class all of these 
    have to be created in the child class then only the class will be 
        implemented during the execution'''


class Square(shapes):
    def __init__(self, side):
        self.side = side 

    def perimeter(self):
        print(4 * self.side)

    def area(self):
        print(self.side * self.side)

class Circle(shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        print(3.14 * 2 * self.radius)

    def area(self):
        print(3.14 * self.radius * self.radius)

obj = Circle(3)
obj.perimeter()
obj.area()


