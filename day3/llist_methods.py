#append()
vowels=["a","e","i","o",]
vowels.append("u") # add u in the list
print(vowels)

#extend
a=[1,2,3]
b=[4,5,6] 
result=a.extend(b) #existing list mai extend vairako result objects ma haina so none aauxa result
print(result) #none because a.extend(b) ko none value return garerako xa
print(a) #a.extend(b) ko value aauxa a ma aauxa so [1,2,3,4,5,6]

#insert(index,value)
vowels=["a","e","o","u"]
vowels.insert(2,"i") #@ index ma i add hunxa
print(vowels)

#remove(value)
a=[1,2,3,4,5]
a.remove(3) #list bata 3 lai hataunxa
# a.remove(6)  #error cuz 6 is not in the list
print(a)

#pop(index)
vowels=["a","e","i","o","u"]
result=vowels.pop(3) #index 3 ko vlaue remove garxa
print(vowels) 
print(result) #o  cuz pop returns o
#opo method doesnot necessarily take a parameter. If parameter is not provided then last item is removed
vowels.pop()
print(vowels)

#clear()
a=[2,3,4]
a.clear() #remove all elements in list
print(a)

#index(value,start,end)  start and end arenot compulsory parameter
vowels=["a","e","i","o","u"]
result=vowels.index("i") #returns the index of the value
print(result)

a=[1,2,3,1,2,4,2]
result=a.index(2,2,5) #start and end nadidia first ma jun 2 vetayo tyei index return garxa
print(result)

#count()
a=[1,2,3,4,5,1,2,4]
result=a.count(4) #returns the no of 3
print(result)


