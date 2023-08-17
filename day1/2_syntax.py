help("keywords") #print all keywords in python
area=1 #case sensitive so area and Area are diff variable
Area=2

####Identifier
# any name of variable, func or class 

##Rules
"""
1. case sensitive
2. cant be keyeords
3. a-z, A-Z, 0-9, _
4. cant start with digit
5. cant use special symbols like @, $, # 
"""

import keyword
keyword.iskeyword("name")
"name ".isidentifier


##Python statement
'''
Each line in python code is statement
we can separate multiple sttements in same line using ;
we can also use back slash for line continuation
'''
a=2; b=3
print("hello" \
      "world")


##### Identation
'''
important to represent a block of code
use of (:) is identation
'''
if a==2:
    print(a)
    if b==2:
        print(b)
    print("hi")
print(a)