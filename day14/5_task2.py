# create a decorator "login_required" which checks the password provided by the user. if the password 
# matches "12334" then the user can access the func else show message "your password is inavlid"

def login_required(func):
    def inner_func(*args):
        if password=="1234":
            return func(*args)
        else:
            return "the password is inavlid"
    return inner_func

@login_required
def password(txt):
    return txt

p=input("enter your password:")
print(password(p))