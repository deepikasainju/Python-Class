#String indexing and slicing is similar to that of list
#Forward indexing starts from 0 and reversing indexing starts from -1

#indexing
m="Hello World"
print(m[0])
print(m[3])
print(m[-1])
print(m[-3])
# print(m[90])   #errors
# print(m[-30])


#slicing
print(m[:5])
print(m[0:5])
print(m[3:])
print(m[2:7])
print(m[7:2]) #empty string aauxa
print(m[:-3])
print(m[0:-3]) #-3 exclude hunxa yesma
print(m[-3:]) #rld
print(m[-2:-7]) #empty string
print(m[-7:-2]) #o Wor
print(m[7:-8]) #empty string
print(m[-8:7]) #lo W

m="Hello world"
# m[2]="L"
print(m) #m ko value change hunna becuz strung is immutable

del m #deletes string

#Iterating through string
m="Hello World"
for each  in m:
    print(each)

for i in m[5]:
    print(i)