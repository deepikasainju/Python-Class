a=[1,2,3,4]
b=a
print(a)
print(b)
print(a is b)
a[1]=3
print(a)
print(b)

a=[1,2,3,4]
b=a.copy()
print(a)
print(b)
print(a is b)


#shallow copy
a=[[1,2,3],4,5]
b=a.copy()
print(a)
print(b)
a[0][1]=7
print(a)
print(b)# 4,5 change garxa b ma change hudaina
#even if b is copy of a, if we change any mutable object inside a then the chnage is also reflected in b

##Deepcopy
from copy import deepcopy
a=[[1,2,3],4,5]
b=deepcopy(a)
print(a)
print(b)
a[0][1]=7
print(a)
print(b) #mutable inside of a is changed but value of b doesnot change