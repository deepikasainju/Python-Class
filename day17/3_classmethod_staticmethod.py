# class methods are the methods which takes class as the final parameter rather than self
# class method is created using @classmethod decorator

# static methods neither taek calss nor self as parameter
# static method is created using @staticmethod decorator
# they are like normal func which doesnt change the state of the class

# # class method
class Student:
    def __init__(self,age):
        self.age=age

    @classmethod
    def from_birth_year(cls, year): # @classmethod use gareko ley cls ma class janca
        age=2023-year
        return cls(age) #Student(age) gareko jastai nai ho

s1=Student(26)
print(s1.age)

s2=Student.from_birth_year(1992)
print(s2.age) 

# here from_birth_year method is a class method. and it is also sometimes termed as "factory method" 


# # Static method
class Student:
    def __init__(self,age):
        self.age=age

    @classmethod
    def from_birth_year(cls, year): # @classmethod use gareko ley cls ma class janca
        age=2023-year
        return cls(age) #Student(age) gareko jastai nai ho
    
    @staticmethod # state lai kei change gardaina. constant kura haru rakhna use hunxa 
    def institute_name():
        return "boardway" 

s1=Student(26)
print(s1.age)

s2=Student.from_birth_year(1992)
print(s2.age) 

print(s2.institute_name())