# concatenation(+)
a=(1,2,3)
b=(4,5,6)
print(a+b) #(1,2,3,4,5,6)

#repition/ broadcast(*)
a=(1,2)
print(a*2) #(1,2,1,2)

# membership operation
print(1 in(1,2,3))
print(1 not in (1,2))

# iteration in tuple is same as that of list
vowels=("a","e","i")
for each in vowels:
    print(each) #("a","e","i")

#unlike list, tuple doesnot have tuple comprehension
a=[i for i in range(5)] #list comprehension
print(a)
a=(i for i in range(5)) # this is generator expression (not tuple comprehension)
print(a)