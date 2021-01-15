"""Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

"""
class FirstClass:
    x=4

obj = FirstClass()
print(obj.x)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fname(self):
        print("my name is :" + self.name)


obj1=Person("Raja",34)
print(obj1.name)
print(obj1.age)
obj1.fname()
obj1.age=23
print(obj1.age)