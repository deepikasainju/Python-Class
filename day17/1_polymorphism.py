# polymorphism refers to many forms of the same func
# sum(), len(), max() etc . are some which follows polymorphism
# These built-in func can take different datatypes and perform teir respective tasks

# there are 2 important aspects of polymorphism
# 1. function /method overloading
# 2. operator  overloading


# function /method overloading
def add(a,b):
    return a+b

def add(a,b,c):
    return a+b+c

# result= add(1,2)
# print(result)    attribute error
result=add(1,2,3)
print(result)

# though add() is defined twice, only the latest definitiion is considered.
# so, python doesnt support function/method overloading

# but we can give default argument so that we can pass both two or 3 arguments in the functional call
def add(a, b, c=0):
    return a+b+c

result=add(1,2)
print(result) # 3
result=add(1,2,3)
print(result) # 6


# for class
class Employee:
    salary=1200

    def description(self):
        return self.salary
    
    def description(self):
        return f"salary:{self.salary}"
    
e=Employee()
print(e.description()) # the last definition is considered. so the result is salary:1200



