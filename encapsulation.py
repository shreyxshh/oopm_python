'''
uptill now all the attributes and methods we created are all public methods and attributes
'''
class Animal:
    name = 'lion' #public 
    _age = 12 #protected
    __height = 120 #private 

    def speak(self): #public
        print("the lion roars")
    def _walk(self): #protected
        print('the lion is walking')
    def __sleep(self): #private
        print('the lion is sleeping')

'''
a protected method and attributes canbe accessed by objects but we still write them
    to tell other programmer to use these accordingly
'''

#public modifiers
obj = Animal()
print(obj.name)
obj.speak()

#protected modifiers
print(obj._age)
obj._walk()

#private modifiers
'''this will give an error bcz a obj cant access a private attribute or method'''
print(obj.__height)
obj.__sleep()

