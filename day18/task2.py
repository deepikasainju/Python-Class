# create a function to check whether a input character is vowel or not. handle the possible exceptions.

def is_vowel(a):
    vowels=["a", "e", "i", "o", "u"] 
    if a.lower() in vowels:         # compressed form = return a.lower() in vowels
        return True                 # if char.isnumeric()      =yesle number ho ki haina check garxa    
    else:                           # if type(char)!= str      =yesle string ho ki haina check garxa
        return False                # if any([char.isnumeric(), len(char)>1, type(char)!=str])                            
    

c=input("enter a character:")
check=is_vowel(c)
if check==True:
    print(f"vowel:{c}")

else:
    print("not a vowel character")
