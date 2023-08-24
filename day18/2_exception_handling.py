# exceptions in python can be handled by using try...except block

try:
    num=int(input("enter a number:"))
except:
    print("something went wrong")


# we can specify the error type init he except statement to catch the specific type of error

try:
    num=int(input("enter a number:"))
except ValueError:
    print("please a valid number")

# we can catch multiple exception using the same except block

try:
    num=int(input("enter a number:"))
except(ValueError, KeyError, TypeError):
    print("please enter a valid number and peform the operation properly")


try:
    num=int(input("enter a number:"))
except ValueError:
    print("please enter a valid number")
except TypeError:
    print("please check your operation")


# try...except..else...finally block
# else block is executed when no error occurs in the try error
# finally block is always executed no matter there is an error or not

try: # error na aaune code try ma narakhi else ma rakhne
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))

except ValueError: # error msg nai print garna:- (except Exception as e) print(e)
    print("please enter a valid number")

else: # error aayena vane else run hunxa. except run vayena vane else run hunxa
    add=num1+num2
    sub=num1-num2
    prod=num1*num2
    print(add)
    print(sub)
    print(prod)

finally: # always executed
    print("this block is always executed")