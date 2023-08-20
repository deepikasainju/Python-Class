# decorators are the func that add extra functionality to the existing function

def decorate_me(func):
    def inner_func():
        print("i am the extra functionality")
        return func()
    return inner_func


@decorate_me # extra functionality   # message=decorate_me(message) the message inside decorate_me is func
def message():
    print("hello world")
message()