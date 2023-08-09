# Tuples are immutable data types. They are sequential
# elements in tuples are enclosed in parenthesis ()


# creating an empty tuple
a=tuple()
print(a)

a=()
print(a)

# creating non empty tuples
a=(1,2,3)
print(a)
a=tuple([1,2,3])
print(a)
a=([1,2],1,"a",{"1":2})
print(a)

a=1
print(type(a))

a=(1)
print(type(a))

a=(1,)
print(type(a))

a=1,   # , haleki tupule hunxa
print(type(a))

