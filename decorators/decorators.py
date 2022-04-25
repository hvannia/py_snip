class decorator_with_arguments:
    def __init__(self, arg1, arg2):
        print("in __init__")
        self.arg1 = arg1
        self.arg2 = arg2
        print("Decorator args: {}, {}".format(arg1, arg2))

    def __call__(self, f):
        print("in_call__")

        def wrapped(*args, **kwargs):
            print("in wrapped()")
            return f(*args, *kwargs)

        return wrapped


@decorator_with_arguments(7, "Python")
def doubler(number):
    return number * 2


print(doubler(5))


def tripler(number):
    """Triples the number passed to it"""
    return number * 3


def info(func):
    def wrapper(*args):
        print("Name: " + func.__name__)
        print("Descrption: " + str(func.__doc__))
        return func(*args)

    return wrapper


my_decorator = info(tripler)
print(my_decorator(3))
