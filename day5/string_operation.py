## Concatenation (+)
m1="hello"
m2="world"
print(m1+m2)

## Repition/ broadcast in string done usung (*)
m="Hello"
print(m*3) #helohellohello

## Membership operation
print("m" in "message")
print("m" not in "message")

## built -in function 
'''
len() =gives length(total no of elements) of sequential data (list,string,etc)
'''
print(len(m))
print(type(m)) #string

 # slice() =similar to list and string slicing
sliced_data=slice(2,4)
print(m[sliced_data])
