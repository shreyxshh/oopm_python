'''
to make many forms of same methods with different functionality is considered as polymorphism
'''

class Animal:
    def speak(self):
        print('the animals are shouting')

class Human:
    def speak(self):
        print('the humen speaks')

obj1 = Animal()
obj2 = Human()

obj1.speak()
obj2.speak()

'''
there are different types of polymorphism
    1. method overriding
    2. method overloading
    '''

#using inheritance with polymorphism we get method overriding

#1. method overriding
class Reebok:
    def __init__(self,material, size):
        self.material = material
        self.size = size

    def details(self):
        print("your bags details are : ")
        print(self.material)
        print(self.size)

class Campus(Reebok):
    def __init__(self, material, size, color):
        super().__init__(material, size)
        self.color = color

    def details(self):
        print(self.color)
        print(super().details())

obj3 = Campus()
obj3.details('leather', 20, 'black')

'''
when child class objet has the power to call methods and attributes 
of a parent class but he cannt call the details method from his parent class cause that 
details because we created another method naming details
and overrides the method which is created in child class
this is the example of method overriding 
'''

#2. method overloading
'''
in python there no overloading bcz its interpreted language and will get '''
class animal:

    def hello(self, a):
        print('hello world')
    def hello(self, a, b):
        print("hello humans")

obj4 = animal()
