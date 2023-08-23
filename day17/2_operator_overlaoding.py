# each operator in python has its own magic method which is called when the operation is carried out
# magic methods in python are the special methods created by using the double underscore
# __add__(), __mul__(), __sub__(), etc 

a=1
b=2
result=a+b
print(result)

result=a.__add__(b)
print(result) # 3

# so everytime an operation is performed a magic method is called.
# magic methods are also called as dunder methods.