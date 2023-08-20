import time
print(time.time())

# create a decorator which calculates the amount of time that it took to execute a func

def time_required(func):
    def inner_func(*args, **kwrags):
        start=time.time()
        result=func(*args,**kwrags)
        end=time.time()
        timereq=end-start
        print(f"execution time: {timereq}")
        return result
    return inner_func

@time_required
def timeloop(txt):
    for i in range (1000000):
        continue
    return txt

print(timeloop("time"))
