# membership operation
# dictionary membership is checked in keys not in values
student={"name":"jon", "age":25}

print("jon" in student) #False bcuz it is checking in value
print("name" in student) #True
print("age" not in student) #False


student={"name":"jon", "age":25}
# len()
print(len(student))

# sorted()
result=sorted(student)
print(result)   # ['age', 'name'] only keys are printed as list

# str()
result=str(student)
print(result) #"{'name': 'jon', 'age': 25}" purai dictionary lai string banai dinxa

# all(sequence)
# all() func takes only one parameter and that should be iterative
# sabai true huna parxa like and
# all the elements inside the iterable must be truthy for all() to return true

data=[1, "hello", [1,2]]
result=all(data)
print(result) #true

result=all([1,2,0])
print(result) #False

# but there one exception in all()
result=all([])
print(result) #true


# any(sequence)
# any() func takes only one parameter and that should be iterative
# any one the elements inside the iterable must be truthy for any() to return true
data=[1,2,0]
result=any(data)
print(result) #true

result= any([0,[]])
print(result) #false

