#class is just a blueprint it doesnt create anything
# class is a blueprint of objects  
class Sharmavishnu:

    """
    function inside the class is called methods
         variable inside a class is called attributes
    """
    def sample():
        print("this is sample functiion")
    
    a = "lol"

#direct calling(public scope)
Sharmavishnu.sample()
Sharmavishnu.sample2()
print(Sharmavishnu.a)

class Animal:
    name = "animal"
    def greet(self):
        print("this is animal class")

"""
we assign the class in any variable
    to make it an object
"""
a1 = Animal()

"""
running this code will give an error which is method wants an parameter to execute but none is pass
here during method callinng with obj we have to pass the obj in the method
"""
a1.greet()
print(a1.name)

"""
a class can have multiple objects 
"""

'''here "self" is just a parameter which is passed to make the method acutally work bcz 
        while calling any method using object we need to always pass 1 parameter which 
            in take the place of obj itself'''

class Interact:
    def greet(self):
        print("this is interact class")

    def greet(self): 
        print("this is second fucntion")    
    def add(self):
        n1 = int(input("enter n1"))
        n2 = int(input("enter n2")) 
        print(f"the sum is {n1 + n2}")

I1 = Interact()     
'''
if in a class two methods of same name exists then the latest function which was created 
    will be executed '''
I1.greet()
I1.add()
