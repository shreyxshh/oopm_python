#objective -> create basic oops program for registration in class 10 and 12

#parent class
class Student:
    def __init__(self, name, age, email, phno):
        self.name = name
        self.age = age
        self.email = email
        self.phno = phno

    def show(self):
        print(f'student details are : {self.name}, {self.age}, {self.email} and {self.phno}')

#child class1
class Class10Admission(Student):
    def __init__(self, name, age, email, phno):
        super().__init__(name, age, email, phno)
        
    def admission10(self):
        print('the admission process is done class 10 and ur in the school')

#child class2
class Class12Admission(Student):
    def __init__(self, name, age, email, phno):
        super().__init__(name, age, email, phno)

    def admission12(self):
        if self.age >= 16:
            print('the admission process is done class 12 and ur in the school')   
        else:
            print('the student doesnt meet the age criteria for class 12 admission' \
            ' so admission fails')
    
print('enter 1 for class 10')
print('enter 2 for class 12')

choice = int(input('enter ur choice : '))

name = input('enter name : ')
age = int(input('enter ur age : '))
email = input('enter ur email : ')
phno = int(input('enter ur phone number : '))

if choice == 1:
    obj1 = Class10Admission(name, age, email, phno)
    obj1.show()
    obj1.admission10()
elif choice == 2:
    obj2 = Class12Admission(name, age, email, phno)
    obj2.show()
    obj2.admission12()