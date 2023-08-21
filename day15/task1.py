# create a class Person with instance attributes name and age.
# create a method get_details in this class to print name and age

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def get_details(self):
        return f"the name is {self.name} and age is {self.age}"
    
p=Person("shyam",23)
print(p.get_details()) 