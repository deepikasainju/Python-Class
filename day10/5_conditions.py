# condtions are used for making decisions in a progarm
# there are 4 varieties of condition we can create
# 1. simple ig
# 2. if..else condition
# 3. if....elif...else ladder
# 4. nested if

''' in the if conditions the statements after the "if" is checked =. if the statement is truthy then
the condition is satisfied and the block inside "if" is executed. otherwise not executed'''

a=20
if a>15:
    print("the number is greater than 15")
else: 
    print("the number is less than 15")
if a:
    print(f"the number is {a}")


# if ..elif..else ladder
marks=78
if marks>=80:
    print("scored distinction")
elif marks>=65:
    print("1st division")
elif marks>=55:
    print("2nd division")
elif marks>=40:
    print("3rd division")
else:
    print("fail")


# nested if
a=20
if a>10:
    if a>15:
        print(f"{a} is gerater than 15")
    else:
        print(f"{a} is greater than 10")
else:
    print(f"{a} is less than 10")


# wap to check if a number is odd or even
n=int(input("enetr a number:"))
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")