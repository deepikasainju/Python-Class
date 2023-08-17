# wap to print first 20 multiple of 3
for i in range(21):
    print(i*3)


# wap to print first 50 even numbers:
count=0
i=0
while count!=50:
    if i%2==0:
        print(i)
        count+=1
    i+=1


# wap to delete all the occurance of a specified character in a given string
# s="all the occurance of a specified character in a given string"
# input="a"
# output=without all "a"
s="all the occurance of a specified character in a given string"
a=input("pick a character:")
b=str() # empty string b="" pani milxa
for i in s:
    if i.lower()==a.lower():
        continue
    b+=i
print(b)


## wap to create a list of repeated items from provided list
# nums=[3,4,2,2,1,3,3,3]
# output=[3,2]
nums=[3,4,2,2,1,3,3,3]
rlist=[]
for i in nums:
    if nums.count(i)>1:
        if i not in rlist:
             rlist.append(i)
print(rlist)