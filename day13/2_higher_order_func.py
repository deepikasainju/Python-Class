# A function that takes another func as an argument is called higher order function
# sorted(), map(), filter(), decorators etc. are the higher order functions in python

## map(function, iterable)
# it takes function as first parameter and iterable as second parameter
# it maps every element of the iterable to some other form
# the len of initial iterable and final result is same in map

data=[1,2,3,4]
def cubed(elem):
    return elem**3

result=map(cubed,data)
print(result) # <map-object> which is an iterator and can be looped.
# but to see its element we need to convert it  to some other datatype
for each in result:
    print(each)
# print(list(result))
# iterable vayeko ley ekchai used garexi feri use garna mildaina


## filter()
# it also takes func and iterable as an argument
# but the size of initial iterable and final result is not same
# it picks certain elements from the initial iterable
data=[1,2,3,4,5,6,7,8,9,10]
def geteven(elem):
    return elem%2==0 #  if elem%2==0:
                         # return True
                    # else:                #yo garnu ra agadi ko garnu same ho
                         # return False

    
result=filter(geteven, data)
print(result) # <filter object>
print(list(result)) # [2, 4, 6, 8, 10]
# if elem is truthy it is picked else not picked


## reduce()
# it also takes func and iterable as an argument
# it does operation based on the function and return a single value
from functools import reduce
data=[1,2,3,4,5]
def add(x,y):
    print(x+y)
    return x+y

result=reduce(add,data)
print(result) # 15 paila 1+2 ani 1+2+3 ani 1+2+3+4 ani 1+2+3+4+5

