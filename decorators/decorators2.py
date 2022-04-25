import time


def fn_timer(func):
    def time_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        diff = time.time() - start
        print(f"{func.__name__}() took {diff}ms")

    return time_wrapper


def count(num):
    for x in range(0, num):
        pass


# w/o timer
count(10000)
# with timer
timed_count = fn_timer(count)
timed_count(10000)


# decorator instead
# decorator is a closure on data function to be executed


@fn_timer
def count(num):
    """Old school sleeper"""
    for x in range(0, num):
        pass


count(10000)

print(count.__name__)  # wrapper not count
# use functools
from functools import wraps


def logit(func):
    @wraps(func)  # wrap the closure
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}()")
        func(*args, **kwargs)
        print(f"Returned from {func.__name__}()")
    return wrapper


@logit
def greet(name):
    # """old school coding tradition"""
    print("Hello", name)


greet("World")
greet.__doc__


