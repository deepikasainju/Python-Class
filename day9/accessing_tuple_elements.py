# we can access tuple element using tuple slicing similar to that of list

# Indexing
vowels=("a","e","i","o","u")

print(vowels[4]) #u
print(vowels[0]) #a
print(vowels[-1]) #u
print(vowels[-3]) #i
#  print(vowels[10])  error out of range
# print(vowels[-10]) error out of range


# Slicing
data=("a","b","c","d","e","f","g","h","i","j")
print(data[:5]) #('a', 'b', 'c', 'd', 'e')
print(data[0:7]) #('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(data[3:]) #('d', 'e', 'f', 'g', 'h', 'i', 'j')
print(data[4:8]) # ('e', 'f', 'g', 'h')
print(data[9:3]) #()

print(data[:-3]) # ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(data[0:-6]) # ('a', 'b', 'c', 'd')
print(data[-7:]) #('d', 'e', 'f', 'g', 'h', 'i', 'j')
print(data[-7:-3]) #('d', 'e', 'f', 'g')
print(data[-2:-6]) #()
print(data[3:-6]) #('d',)
print(data[-8:7]) # ('c', 'd', 'e', 'f', 'g')

print(data[2:9:2]) #('c', 'e', 'g', 'i') 
#here the last parameter is a step size. If "2" is given it jumps by one step size

#delete 
del data # deletes the object