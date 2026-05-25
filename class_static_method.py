#1. classmethod
class Animal:

    name = "dog" #class attribute
    '''to change the class attribute an obj is not capable to do so
            then we create a classmethod which takes in class as the paramter 
                and will apply the changes'''
    #instance can never your class attribute
    #syntax to create a class method
    @classmethod 
    def change(cls, new):
        #here we are passing the whole class which allows the "change" method to change the "name"
        cls.name = new
        print(cls.name)

lion = Animal()
print(Animal.name)
lion.change("shreyash")
print(Animal.name)


#2. staticmethod
class SharmaVishnu:

#to run this function without passing any "self" or object we can use "@staticmethod"
#staticmethod are independent of object, means to call this function we dont need any object to be called 
    @staticmethod
    def menu():
        print("paneer tikka") 
        print("paneer sabzi") 
        print("paneer sandwich")

new_market = SharmaVishnu()
new_market.menu()

#3. object method 
'''this is the normal method which we call using object and be accessed using objects'''