# copy()
s1={1,2,3,4,5}
s2=s1.copy()
print(s1)
print(s2)

# set ma shallow copy hudaina deep copy matra hunxa kina vane set ko elements immutable hunxa

# difference()
s1={1,2,3,4,5,6}
s2={4,5,6}
diff=s1.difference(s2)
print(diff)
diff=s1-s2
print(diff)

# union()
s1={1,2,3,4,5,6}
s2={4,5,6,7}
u=s1.union(s2)
print(u)
u=s1|s2
print(u)

# intersection()
s1={1,2,3,4}
s2={2,5,6}
i=s1.intersection(s2)
print(i)
result=s1&s2
print(result)

# isdisjoint()
s1={1,2,3,4,5,6}
s2={5,6,7,8}
print(s1.isdisjoint(s2))

# issubset
s1={1,2,3,4,5,6}
s2={5,6,7,8}
print(s2.issubset(s1))
s3={4,5,6}
print(s3.issubset(s1))
print(s1.issuperset(s3))

# symmetric difference
s1={1,2,3,4,5,6}
s2={5,6,7,8}
result=s1.symmetric_difference(s2)
print(result)
result=s1^s2
print(result)

# symmetric difference update
s1={1,2,3,4,5,6}
s2={5,6,7,8}
s1.symmetric_difference_update(s2)
print(s1)

