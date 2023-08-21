# inheritance is the process of accessing the attributes in the parent class by childern classes
# types of inheritance in pyhton
# 1. single inheritance
# 2. multiple inheritance
# 3. multilevel inheritance
# 4. hierarchical inheritance
# 5. hybrid inheritance

# single inheritance
class A: # parent class
    a=2

class B(A): # child class
    pass

obj=B()
print(obj.a) # 2


# multiple inheritance
# multiple parent ko euta child
class A:
    a=3

class B:
    a=5

class C(A,B):
    pass
obj=C()
print(obj.a) # 3


# multilevel inheritance
class A:
    a=5

class B(A):
    a=10

class C(B):
    pass

obj=C()
print(obj.a) # 10


# hierarchical inheritance
# euta parent ko multiple children
class A:
    a=5

class B(A):
    pass

class C(A):
    pass


# hybrid inheritance
# combination of multiple and hierarchical inheritance

# cross shape
class A:
    a=5

class B:
    a=3

class C(A,B):
    pass

class D(C):
    pass
class E(C):
    pass


# diamond shape
class A:
    a=3

class B(A):
    pass
class C(A):
    pass

class D(B,C): # B paila inherit gareko ley B ma paila khojxa
    pass
obj=D()
print(obj.a)

# MRO stands for method resolution order. 
# it is the order in which attributes in an inheritance is accessed from the child class
print(D.mro()) 


