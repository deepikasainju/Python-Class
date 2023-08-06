
print(list(range(7)))
for value in range(7):
    print(value)

    
#create a list of first 10 multiples of 3 using list comprehension
a=[]
for i in range(1,31):
    if i%3==0:
        a.append(i)
print(a)

a=[i*3 for i in range(1,11)]
print(a)

