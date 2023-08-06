#True and False are the boolean data types in python 
#represent true state and false state respectively

## Operators that gives boolean type
#Comparison
a=4
b=5
print(a>b)
print(a==b)
print(a<b)
print(a!=b)

#Logical operation
a=5
a=4
print(a>b and b!=a)
print(a!=b or a>b)
print(not a)
print(not True)
print(not False)

#Membership operation
print("a" in ["a","e","i"])
print("i" not in ["a","e","i"])

#identiy opration
a=1 # duitai eutai memory ma store hunxa tara value is big vane arko location ma save hunxa
b=1
print(a is b) #euta limit sama matra a is b true aauxa ie a=1845 b=1845 vako vaye ais b false aauxa
print(id(a) == id(b))
print(a is not b)
print(id(a)!=id(b))
print(id(a) is id(b))


###Concept of Truthy and Falsy
a=5
print(not a) #False
#any non zero and non empty including True itself is a Truthy data type
# 5,-1, [1,2], (1,4), {1,2,"a"}, {"a":1}, True are truthy data types
# in contrast all empty data types, zero and None and False are falsy data types
# 0,[], (), {}, '', None, False are falsy data types
 
##How we verify Truthy and Falsy?
#Check for truthy
a=1
b=[1,2]
c=(1,2)
d={"a":1}
e="Hello World"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(True))
print(bool(e))

#Applying not operation in truthy value return False
print(not a)

#Check for Falsy
a=0
b=[]
c=()
d={}
e=''
f=set()
g=False
h=None
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))
print(bool(h))
print(bool())

#applying not in falsy value return True
print(not a)
print(not None)


### Python boolean is a subclass of integer
#True is a integer 1 and False is integer 0
print(True +1)
print(10*False)
print(True + True)
print(False + False)

