#sort(reverse=True, key=function) method
a=[2,5,6,2,3,1,8]
a.sort() #return is none  #list is sorted
print(a) 

a.sort(reverse=True) #sorted in descending order
print(a)


a=[(5,4),(3,2),(4,10),(12,1),(1,9)]
#paxadi ko number(parameter) ko base ma sort huna paryo

def get_sec_num(data):
    return data[1]
a.sort(key=get_sec_num)
print(a) #[(12, 1), (3, 2), (5, 4), (1, 9), (4, 10)]


a=[(4,12,5),(6,1),(11,12),(6,7,8)]
def last_num(data):
    return data[-1]
a.sort(key=last_num)
print(a)
a.sort(key=last_num, reverse=True)
print(a)

#reverse()
a=[1,2,6,7,3,4]
a.reverse() #return none
print(a)

