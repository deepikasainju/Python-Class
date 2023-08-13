#  wap to find greatest among 3 numbers
print("enter 3 numbers:")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is the greatest number.")
elif b>a and b>c:
    print(f"{b} is the greatest number.")
else:
    print(f"{c} is the greatest number.")


# wap to prompt the user for hours and rate per hour using input to compute gross pay. 
# pay the hourly rate for the hours upto 40 and 1.5 times the hourly rate for all hours worked 
# above 40 hours. use 45 hours and rate per hour 10.50  pay should be 498.75

hours=int(input("enter hours:"))
rate_hour=float(input("Enter rate per hour:"))
if hours<= 40:
    pay=hours*rate_hour
elif hours> 40:
    remain=hours-40
    pay=40*rate_hour+remain*rate_hour*1.5
print(f"total pay is {pay}")