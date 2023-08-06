'''
list are mutable and are sequential
created enclsing data in []
'''

#creating empty list
a=[]
b=list()

#creating non empty list
a=[1,2,3]
vowel=["a","e","i","o","u"]
#example of homogeneous data types

#heterogeneous data types
a=[1,2,["a","e"],("i",3),{1,2,3},{"q":1,"b":2}]

##Accessing list items
#list item can be accessed using idexing and slicing

#Indexing in list starts from 0 for forward traverse and -1 for backward traverse
vowels=["a","e","i","o","u"]
print(vowels[0]) #a
print(vowels[2]) #i
print(vowels[4]) #u

print(vowels[-1]) #u
print(vowels[-3]) #i

## print(vowels[10]) #list index out of range error
## int(vowels[-8]) #error


#item assignment is possible in list as it is mutable
vowels[1]="E"
print(vowels)


##List slicing
a=["a","b","c","d","e","f","g","h","i","j"]
print(a[0:5]) #0 to 5 index sama ko value matra print hunxa
print(a[:5])
print(a[7:2]) #[] ie khali aauxa
print(a[2:]) # 2 index dekhi sabai print hunxa

print(a[2:9])

print(a[0:-2]) #last ko duita exclude garxa
print(a[:-2])
print(a[-5:]) # f dekhi sabai print hunxa
# print(a[-7:-2])
print(a[2:-1])


###List operations
#concatenation
a=[1,2,3]
b=[4,5,6]
result=a+b
print(result)

#Membership operations
print(2 in [1,2,3]) #true
print(3 not in [1,2,3]) #false


