#types of inheritance:-
'''
1. single inheritance
2. multiple inheritance
3. multilevel inheritance
4. hierarchial inheritance
5. hybrid inheritance
'''

#single inheritance
class Parent:
    def __init__(self):#constructor
        print('this is parent class constructor')

    def greet(self):    
        print('this is parent class')

class Child(Parent):
    def __init__(self):
        print('this is child class constructor')

    def show(self):
        print('this is child class')
obj = Child() 
#always create the obj of child class or the class which is inheriting 
obj.greet()
obj.show()

class Factory:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(f'bag has {self.name} and {self.color} color')

class Bata(Factory):
    def __init__(self, name, color, zip , pockets):
        super().__init__(name, color)
        #super(). -> is used to get all the variable and fucntions which are present in the parent class and 
        #those canbe accessed using this "super()"

        '''this can only be used in single class inheritance'''
        
        self.zip = zip
        self.pockets = pockets

    def display(self):
        print(f"Bag has {self.name}, {self.color}, {self.zip} zips and {self.pockets} pockets")

Bag = Bata('Shreyash', 'Black', 2, 12)
Bag.display()

'''in single inheritance we just have one child and one parent class'''

#multiple inheritance
class Father: #parent 1
    def __init__(self):
        print('this is father constructor')

    def mother_greet(self):
        print("this is father class")

class Mother: #parent 2
    def __init__(self):
        print('this is mother class constructor')

    def father_greet(self):
        print("this is mother clas")

class Child(Father, Mother): #child
#which ever class was passed first, that class's constructor will run in this case "father" class 
   
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
'''using this we can call constructors from specific class
        super() cant be used here bcz there is multiple inheritance'''

obj = Child()
obj.father_greet()
obj.mother_greet()

#mutlilevel inheritance
'''
class A -> class B -> class C   and so on,,,,,,,,,
in this type of inheritance multiple classes are inherited in a single class in multiple level
one child class become parent of another class
'''

class A: #Super Parent
    def greet(self):
        print("this is class A")

class B(A):#Parent class
    def show(self):
        print("this is class B")

class C(B):#Child class
    def details(self):
        print('this is class C')

obj = C()
obj.greet()#present in class A
obj.show()#present in class B
obj.details()#present in class C


class CEO:#super parent class
    def __init__(self):
        print("this is CEO class")

class Manager(CEO):#parent class 
    def __init__(self):
        super().__init__()#used to call constructor from Parent class
        print("this is manager class")

class Employee(Manager):#child class
    def __init__(self):
        super().__init__()
        print("this is employee class")

obj = Employee()
#CEO constructor -> manager constructor -> employee constructor

#hierarchial inheritance
'''
in this type of inheritance there is one parent class is inherited by 
    multiple child classes'''

class Parent:
    def greet(self):
        print('this is parent class')

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj1.greet()
obj2 = Child2()
obj2.greet()
'''these classes can only access parent class and not each other bcz one child class is not 
    inherited in other child class'''



class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def details(self):
        print('this is Account class constructor')

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        print(f'this is saving class constructor {self.name}, {self.balance}')

class Current(Account):
    def __init__(self, name, balance, type):
        super().__init__(name, balance)
        self.type = type
        print(f'this is current class constructor {self.name}, {self.balance} and {self.type}')

obj = Current("shreyash" ,30, 'current')
obj.details()


#hybrid inheritance
'''its the combination two type of inheritance'''

