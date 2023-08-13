# range ()
# can take 3 parameters
# syntax:range(start,end,step_size)
# "end" parameter is always exclusive

data=range(4)
print(list(data))
print(list(range(0,4)))

data=range(2,7)
print(list(data))

data=range(2,10,2) # ek step jump garera print hunxa
print(list(data))


# enumerate()
# in c and c++ looping is done in the index of an array
# unlike c or c++, looping is done in the elements of list/array
# but in python we can use "enumerate " to get the index in each iteration

vowels=["a","e","i","o","u"]
print(enumerate(vowels)) # <enumerate object>
data=list(enumerate(vowels)) # [(0, 'a'), (1, 'e'), (2, 'i'), (3, 'o'), (4, 'u')] 
# index ra value sangai aauxa
print(data)

for index,value in enumerate(vowels):
    print(index) # 0,1,2,3,4
    print(value) # a,e,i,o,u

for index, value in enumerate(vowels,start=1): # index 1 dekhi suru gardinxa
    print(index)
    print(value)


