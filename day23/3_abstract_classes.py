# abstract classes cannot be instantiated 
# this is created using "ABC" moduke from python built-in

from abc import ABC, abstractmethod # abstractmethod is decorator

class Animal(ABC):
    # this is an abstract class
    # it has no object like self

    def sleep(self):
        print("sleep")

    @abstractmethod # this is decorator
    def sound(self):
        pass

a=Animal()

def Dog(Animal): # child class ma abstractmethod ko function hunai parxa
    def sound(self): # decorator vayeko parent class ko func lai override garnai parxa
        print("bark")

def Cat(Animal):
    def sound(self):
        print("meow")

dog=Dog()
dog.sound()
dog.sleep()