# encapsulation is the process of data hiding in oop
# we can make the attributes private,public, and protected

class Vehicle:
    _color="blue" # this the protected property 
    __milage=50 # this is a private property

    def __init__(self,doors,speed):
        self._doors=doors # protected members
        self._speed=speed # protected members
    
    def description(self):
        return f"color is {self._color}, doors is {self._doors} and speed is {self._speed}"
    
    def set_color(self,color):
        self._color=color

    def get_color(self):
        return self._color

v1=Vehicle(4,120)
print(v1._color) # accessing protected member outside the class which is not recommended

v1.set_color("green")
print(v1.get_color())
print(v1.description())

# protected members of a class are meant be used within a class or in their children class only
# they are not meant to be used outside class
# python is not strict in oop approach so it allows protected members to be accessed even outside the class.
# but it is not recommended for developers as it doesnt follow proper convention

# private property is not accessible outside the class or in their children
# print(v1.__milage) ## attribute error
print(dir(v1)) # kun kun class ko access garna milxa dekhauxa
print(v1._Vehicle__milage)  #yesari garda private element lai ni access garna milxa

# though __milage is a private property , we can access it using '_Vehicle__milage'
# it is also called "name mangling" in python