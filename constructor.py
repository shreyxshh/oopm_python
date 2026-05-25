#constructor - 
    # if a constructor function exists in the class no matter its location in the class
    # it will always be executed during the execution face 
    # its executed when one creates a ibj from the class

#instance/object attribute-
    #its created with the help of an obj inside the class
    #its also called via the created object
class Kfc:

    def __init__(self, name, age):
        #to create any function as constructor we use(__methodname__)
        #__init__ -> constructor(dunder fucntion)
        #if two constructor exists the latest one will always be executed
        print("this is constructor function")

        '''obj attributes'''
        self.name = name
        self.age = age

    def menu(self):
        print(self.name)
        print(self.age)
        print("boneless")

#name and age have to passed while the obj is created
obj = Kfc('shreyash', 20)
obj.menu()

#question 
'''make a class which will take two no as input 
    1. 2 instance function
    2. create a function which will print the largest amg them'''

class Addit:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def maxAmg(self):
        print(f"the max amg them is {max(self.n1,self.n2)}")

n1 = int(input("enter n1 : "))
n2 = int(input("enter n2 : "))
obj2 = Addit(n1, n2)
obj2.maxAmg()

