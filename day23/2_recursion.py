# if a function is called from the definition of the same function then it is called as a recursive function

c=0
def count():
    global c # bahira ko c func ma access garna lai global use gareko
    print(c)
    if c==10:
        return
    c+=1
    count()

count()

# wap to find factorial of 5 in three ways
# normal loop
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)

# reduce() function
from functools import reduce
result=reduce(lambda x,y: x*y ,range(1,6))
print(result) 

# recursion
def fact(a):
    if a==0 or a==1:
        return 1
    return a*fact(a-1)
print(fact(5))

# 5*fact(4) =5*24 =120
# 4*fact(3) =4*6 = 24
# 3*fact(2) =3*2 =6
# 2*fact(1) =2*1 =2