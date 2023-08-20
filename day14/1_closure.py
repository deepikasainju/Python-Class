# closure is the concept in python whichh fullfills the following:
# 1.there should be a nested function
# 2. an innere efunc must reference the argument from outer func
# 3. outer func should return the inner func

def closure_func(msg):
    def inner_func():
        print(msg) # yaha closure func ma vayeko arguments use garna parxa
    return inner_func

result=closure_func("hello world") # result=inner_func jastai vayo ie reference leko ho 
result()
# the above func is the simplest closure that can  be made in python.
# closures are the basis of decoraters in pyhton

