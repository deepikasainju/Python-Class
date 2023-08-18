# lambda are the element way of creating one-liner function
# lambda functions do not hve name. so they are also called anonymous function

def squared(num):
    return num**2

print(squared(2)) #6

squared=lambda num:num**2
print(squared(6)) #36


# lambda is called inside map(), filter() and reduce()
# lambda use for map()
data=[1,2,3]
result=map(lambda elem:elem**3, data) # cubed()
print(list(result))
r=map(lambda x:x%2==0, data) # [False, True, False]
print(list(r))

# lambda for filter()
data=[1,2,3]
result=filter(lambda elem:elem%2==0, data) # geteven()
print(list(result))
result1=map(lambda elem:elem**3, data) # cubed() 
print(list(result1)) # sabai value aauxa kina vane elem**3 values are truthy 

# lambda use for reduce()
from functools import reduce
data=[1,2,3]
result=reduce(lambda x,y:x+y, data) # add()
print(result)