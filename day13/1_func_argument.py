# order of the function is important to note
# arguments are the values passed during fucntion call and parameter are the values taken 
# in function definition


## order of the arguments
# 1. positional arguments / compulsory arguments
# 2. default arguments
# 3. arbitary arguments

def add(a,b,c=10): # here a, b are the positional arguments
    return a+b+c

print(add(1,2))
print(add(b=1,a=2,c=5)) # a ma 2 and b ma 1 janxa. These are keywords arguments

# if we send value in the function call then the default value always gets override 
# here c=5 override c=10

## Arbitary arguments
# arbitary arguments can take random number of elements in func call 
# htey are like expandable bucket
def add(*args):
    print(args)
    print(type(args)) #tuple
    return sum(args)

print(add(1,2))
print(add(1,2,3))
print(add(1,2,4,5))

 

def add(**kwargs):
   print(kwargs)
   print(type(kwargs)) #dictionary. ** used for dictionary
   return sum(kwargs.values())

print(add(a=1,b=2)) #3
print(add(a=1,b=2,c=3)) #6


# arbitary argumetns also have its own order. *args should always come beore than **kwargs
def add(a,b,c, d=1, e=2, f=3, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)
    return a+b+c+d+e+f+sum(args)+sum(kwargs.values())

print(add(4,5,6,7,8,9,10,11,12,13,p=1,q=2))