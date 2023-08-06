###operators
#operators are the symbols in python or in any programming language that carry out arithmetci and logical operations
# the python operators are 
# 1. Arithmetic operators
# 2. Raltional operators
# 3. Logical operators 
# 4. Membership
# 5. Identity 
# 6. Assignment

##Arithmetic operators
# 1. Addition
a=4
b=2
print(a+b)
# here a and b are the operands

print(a-b)
print(a/b)
print(a*b)
print(a%b) #gives remainder
print(5%2)
print(a**2) #power

#floor division(//) omits decimal value from divison operation and gives floor value
print(3//2) #1
print(-3//2) #-2 because -1 is greater than -2 

##Relational Operators or Comparison
# ==,<,>,<=,>=,!= 
#gives boolean results ie either true or false
a=3
b=3
print(a==b) #True
print(a<b) #false
print(a>b) #false
print(a!=b) #false

##Logical operators
# and or not
print(a>b or b!=a)
print(a>b or a==b)
print(not True)
print(not False)

a=5
print(not a)

a=0
print(not a) #using the concept of truthy or falsy

##Assignment operators
# is equals to (=)
a=2+3 #2 and 3 are added and assigned to a

a=1
a=a+1 #2
a+=1 #3  +=, -=, *=, /=, %=, //= are also assignment operator

a=2
a%=2 #0
print(a)

##Membership operator
# in , not in    # used in sequence data types
print(2 in [1,2,3]) #True
print(3 not in [1,2,3]) #False
print("p" in ["python"])

##Identity operators
# is, is not     #eutai ho vane true 
a=[1,2,3]
b=a
print(a is b) #true
print(id(a)==id(b)) #true

b=a.copy()
print(a is b) #false cuz value is same but object is diff ie in diff memory location
print(id(a)==id(b)) #false

id(None) #always same id cuz it is always only one not multiple

##Precedence and associativity 
#if operation has multiple operators then precedence defines the order of operator
#same precedence then operation is done based on associativty
# normally all operators have left-right associativity except**
print(2*3/3) #6 multiplication then dicvision is done
print(2**3**2) # 3**2 then 2**9    associativity is from right-left
