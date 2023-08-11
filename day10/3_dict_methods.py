# copy()
student={"name":"jon", "age":25}
s1=student.copy()
print(student)
print(s1)

# get()
student={"name":"jon", "age":25}
name=student.get("name")
print(name)

name=student["name"]
print(name)

roll=student.get("roll") #none
# roll =student["roll"]  keyerror

roll=student.get("roll",5)
print(roll) #5 defult value 5 aauxa

name=student.get("name","jane")
print(name) #jon  dictionary ko valu elai priority hunxa default vanda


# items()
student={"name":"jon", "age":25}
print(student.items()) # dict_items([('name', 'jon'), ('age', 25)]) list vitra dict aauxa
# it cant be used as list but loop can be applied

# keys()
student={"name":"jon", "age":25}
print(student.keys()) #dict_keys(['name', 'age'])

# values()
print(student.values()) #dict_values(['jon', 25])
