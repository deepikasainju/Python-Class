# add()
a={1,2,3}
a.add(4)
print(a)

# update()
a={1,2,3}
a.update([4,5,6])
print(a)

# remove()
a={1,2,3}
a.remove(1)
print(a)
## a.remove(8) garda error aauxa bcuz no element 8

# discard()
a={1,2,3}
a.discard(2)
print(a)
a.discard(6) #no error
print(a)

# pop()
s={1,2,3,4,5,6}
s.pop()
print(s) #randomly pop out any one element

# clear()
s.clear()
print(s) #{}
