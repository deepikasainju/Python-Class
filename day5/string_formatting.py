# we do string formatting using f-string

p= "python"
m=f"i am learning {p}"
print(m)

a=input("enter a language: ") #user ley input diyeko string ko rup ma hunxa even if 14  is inputed
# for integer user input 
### a=int(input("enter a number: "))
m=f"i am learning {a}"
print(m)

a="john"
b=23
print(f"i am {a}. i am {b} years old") #used more nowadays


print("i am %s. i am %d."%("john",23)) #purano method
print("i am {}".format(a)) #purano method
print("i am ",b, "years old") #concatenation jastai ho yo and takes more space

