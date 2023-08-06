#String are immutable 
#They are sequential 

## Creating empty strings
a=""
b=''
c="""

"""  #Doc string/ triple quoted string
d='''

''' 
e=str() #built-in function

##Quote characters
s="i'm learning python" #double outside and single quote inside
# s='I"m learning python' ##This is error
s='he said, "I am hungry"'  #single quote outside and double quote inside


# but we have a feature of escape sequence in pyhton if we want to use a single quote both inside and outside
s='I\'m hungry' #here / is escape sequence
s="he said, \"i am hungry\""

#escape sequence supress the usual meaning of character and gives new meaning
print("hello\nworld")
print("hello\tworld")


### Triple quoted strings
'''Triple quoted string can be used as docstring. We can write docs for function and classes using 
triple quoted string
They are also used as multilined comment
'''

def add(a,b):
    """
    :param a: first integer
    :param b: second integer
    :return: sum of a and b
    """
    return a+b
print(help(add))


s="""shafiuehrnfafheriuhferjlfhi
euhrfnieurhfeirjkfiuerhnfreiuhfanrjkhf
iuaerhnjahfiouaerhfaiuaerhaoiuhfieurhfuierhf
niueorahaaierufhiuaehreihfhiouearhfoeuiahjkferhuihfieru"""
# This a long string
