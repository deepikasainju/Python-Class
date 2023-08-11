# wap to take radius as input and calculate area of the circle
radius=float(input("enter radius:"))
pi=3.14
area=pi*radius**2
print(area)

#wap to find frequency(count) of the input number in a list [5,2,3,5,2,3,3,1,4]
a=[5,2,3,5,2,3,3,1,4]
n=int(input("enter number:"))
print(a.count(n))

# wap to find circumference of circle
radius=float(input("enter radius:"))
pi=3.14
circum=2*pi*radius
print(circum)

# split()
numbers=input("enter numbers:")
num1,num2,num3=tuple(numbers.split(","))
print(num1)
print(num2)
print(num3)