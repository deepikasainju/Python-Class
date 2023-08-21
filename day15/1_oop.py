# oop is an aproach of programming in which programs are modeled in the real world problems
# oop stands for object oriented programming
# it has 2 major aspects: class and objects
# class is the blue print of an object. it has its own attirbutes known as properties and methods
# objects are the instances of class

# thre are 4 major pillars of oop:
# 1. inheritance
# 2. encapsulation
# 3. polymorphism
# 4. abstraction

class Vehicle:
    engine_type="petrol" # class attribute
    
    def __init__(self, no_of_doors, color): #this is a constructor
        self.no_of_doors=no_of_doors  # instance attribute
        self.color=color # instance attribute

    def description(self):
        return f"vehicle engine is {self.engine_type} engine. it has {self.no_of_doors}"\
        f"and color is {self.color}"

# self vaneko vehicle object ho (self.color vaneko vehicle.color nai ho)
# self are for instance atttributes not class attributes

vehicle1=Vehicle(4, "red") 
print(vehicle1.engine_type) # petrol
print(vehicle1.no_of_doors) # 4
print(vehicle1.color) # red
print(Vehicle.engine_type) # petrol (it can be accessed thorugh class name becuz it is a class attribute)
# print(Vehicle.engine_type) ## attribute error
print(vehicle1.description())

# In this Vehicle class "enigine_type" is a class attributes and 
# color and no of doors are the instance attributes and __init__ is constructor


# class has properties and method which are collectively termed as "attributes"

# lets set attribute in the objects
v2= Vehicle("2","green")
print(v2.color) # green (getting the value with the object)
v2.color="red" # setting the value from the object
print(v2.color) # red
