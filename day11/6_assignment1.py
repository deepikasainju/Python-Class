# wap that accepts an integer and computes the value of n+nn+nnn+..
n=int(input("enter an integer:"))
sum=0
for i in range(1,6):
    sum+=n**i
    print(sum)
print(sum)

# wap to calculate difference between a given number and 17. if the number is greater 
# than 17 return twice the absolute difference
n=int(input("enter an integer:"))
if n>17:
    diff=2*abs(n-17)
    print(diff)
else:
    diff=abs(n-17)
    print(diff)

# wap to check whether input number is prime or not
n=int(input("enter an positive integer:"))
count=0
if n==0 or n==1:
    print(f"{n} is not a prime number.")
else:
    for i in range(2,n+1):
        if n%i==0:
            count+=1

    if count>1:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number.")