# namespaces determine the scope of the variables and objects in python
# namespaces is explained by LEGB rule (local, enclosed, global, built-in)
# there are 4 types of namespaces 
#  1. local scope
#  2. enclosed scope
#  3. global scope
#  4. built-in scope


# built-in scope
# if the scope of package or object is all over the project then it is an object of built-in scope
# examples: python built-in libraries like main, os, json
import math  # built-in scope


# global scope
# if the scope of the variable or object is limites to one pyhton module 
# then it has global scope to that module
a=12 # the vairable 'a' is limited to this python file only


# limited scope
# if the variable is limited to a function then it is has local scope
a=12 #global scope
def test_func():
    a=20 # local scope
    print(a)

print(a) #12
test_func() # 20
print(a) # 12


# enclosed scope
# if the scope of the variable or object is limited to nested function then it has enclosed scope
a=12 # global scope
def outer_func():
    a=20 # local scope
    def inner_func():
        a=30 # enclosed scope
        print(a) # 30
    inner_func()
    print(a) # 20

print(a) # 12
outer_func()  
print(a) # 12


# we have a "global" keyword which can define even a local variable as a global
a=20
def outer_func():
    global a
    a=40 # yo a lai global banayo global use garera
    def inner_func():
        a=30
        print(a) # 30
    inner_func()
    print(a) #40

print(a) # 20
outer_func()
print(a) # 40


# non local keyword 
a=20
def outer_func():
    a=40 
    def inner_func():
        nonlocal a # function vari ko lagi a ko value global hunxa
        a=30
        print(a) # 30
    inner_func()
    print(a) #30 nonlocal use gareko ley a ko value change vaisakyo

print(a) # 20
outer_func()
print(a) # 20
