# create a func that takes message and simply return the text message
# create a decorator which changes the text message into the upper case text

def to_upper_case(func):
    def inner_func(*args, **kwargs):
        result=func(*args, **kwargs)
        if type(result)!=str:
            return result
        else:
            return result.upper()
    return inner_func

@to_upper_case
def message(txt):
    return txt

print(message("hello world"))