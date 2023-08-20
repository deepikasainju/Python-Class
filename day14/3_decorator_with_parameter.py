def decorate_me(func):
    def inner_func(*args, **kwargs): #yo func first mai chaldaina return paila chalxa
        print("i am the extra functionality")
        return func(*args) #yo func vaneko message func call garnu ho
    return inner_func # inner func lai call greko


@decorate_me
def message(txt):
    return txt

print(message("helloo world")) # first ma decorate_call hunxa

@decorate_me
def msg2(txt1,txt2,txt3="default"):
    return txt1+txt2+txt3

print(msg2("hello ", "world ",txt3="me"))