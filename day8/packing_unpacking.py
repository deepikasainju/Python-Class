# tuples in python can be packed and unpacked

# Packing of tuple
vowels="a", "e", "i" ,"o", "u"  #yo ni tuple nai ho
print(vowels) #('a', 'e', 'i', 'o', 'u')

a=1,2
print(a) #(1,2) tuple packing
print(type(a)) #tuple


# Unpacking
a,b=1,2 #right side ma packed left side ma unpacked
print(a)
print(type(a)) #int
print(b)
print(type(b)) #int

a,b=(1,2)
print(a)
print(type(a)) #int
print(b)
print(type(b)) #int


# possible error in packing and unpacking
## a,b,c=1,2   not enough value to unpack
## a,b=2,3,4   too many values to unpack
