'''
these are the methods which works on the objects and are used in many ways 
    dunder methods are used to implement abstraction also as it hides the 
        implementation part of the code
'''

class Robots:
    def __init__(self, name):
        self.name = name 

#this will be called whenever we try to print the object else there will be an error
    def __str__(self):
        return f"hello my name is {self.name}"
    
obj1 = Robots('alpha1')
obj2 = Robots('alpha2')

print(obj1)
print(obj2)


class Numbers:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):#when the two objects are used to add together
        return self.value + other.value
    
    def __eq__(self, value):#when two objects are compared to each other 
        return self.value == value.value
    
a = Numbers(10)
b = Numbers(20)

print(a + b)
print(a == b)

#these methods are called autoamtically when the required conditions are met
