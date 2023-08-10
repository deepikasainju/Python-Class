# tuples are immutable so dont havw methods like append(),pop(),insert(),etc.
# the only methods are count() and index()

vowels=("a","e","i","o","u","a","e","o","u")
result=vowels.count("a")
print(result)

result=vowels.index("a")
print(result)
result=vowels.index("a",2,7)  # 2 dekhi 7 ko ma a ko index dinxa
print(result)

#sum()
result=sum((1,2,3,4,5))
print(result)

# max()
print(max(1,4,6,8))

#min()
print(min(1,3,12,6))

#sorted()
a=(3,4,1,6,3,6)
print(sorted(a))
print(sorted(a,reverse=True)) #descending order

#sort() ma return none so result=a.sort() grda result none aauxa sort list ma matra kaam garxa

#reversed()
a=(1,2,5,7,8)
print(reversed(a)) #<reversed object at 0x0000014DBDFD3FA0>
result=reversed(a)
print(list(result)) #reversed object lai print garn alai list ma type cast gareko tuple lai




