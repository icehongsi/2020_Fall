import time

def time_counter(func):
    def timecount(*args, **kwargs):
        before = time.perf_counter()
        func(*args, **kwargs)
        print(f"Time elapsed: {time.perf_counter() - before}")
    return timecount

@time_counter
def fibo3(n):  # extremely inefficient algorithm (exponential growth)
    if n <= 1: return n
    return fibo3(n - 1), fibo3(n - 2)


fibo3(10)