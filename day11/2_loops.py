# loops are used to execute certain blocks of code
# they reduce mannual efforts in the algorithms

# for loop in diff data types
vowels=["a","e","i","o","u"]
for i in vowels:
    print(i)
else:
    print("this is executed if the main loop is completely iterated.")

# looping is similar to list in tuples and set

# loop in dictionary
student={"name":"jane", "age":34, "address": "KTM"}

# looping dictionary keys
print(student.keys()) # ['name', 'age', 'address']

for key in student.keys():
    print(key)

# looping in dictionary values
print(student.values()) # ['jane', 34, 'KTM'])
for value in student.values():
    print(value)

# looping in dictionary keys and values
print(student.items()) # [('name', 'jane'), ('age', 34), ('address', 'KTM')]
for key,value in student.items():
    print(key)
    print(value)


