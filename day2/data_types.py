'''
data types:
number -im
boolean -im
list -m
tuple -im
string -im
dictionary -m
set -m

3 things to keep in mind:
operators
methods
built-in functions

except numbers and boolean, other are sequential like list, tuple and strings
'''

###Mutable and Immutable objects
'''
if an object once created can be altered in its life period then it is mutable data type
example of mutable objects are list, dictionary, set
but if it cant be altered then it is immutable
example of immutable objects are numbers, boolean, tuples, string
'''

a="hello"
b=[1,2,3]
print(a[0])
print(b[0])

a=[1,2,3,4]
a[1]=4 #value is changed
b=(1,2,3,4)
b[1]=4 #error is found cause tuple is immutable

#changing mutable inside immutable
a=(1,2,[3,4])
a[2][0]=5
a
(1, 2, [5, 4])

#Integer
a=9
b=0
c=-1
d=0xA2 #hex
e=0b1011 #octal
f=0o27

#Float
a=2.1
b=-2.3
c=2e3 # 2*10**3
d=2e-3 # 2*10**-3

#Complex
a=1+3j
b=2-5j
c=2j
d=-3j

print(type(a))