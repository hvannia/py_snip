# passing a parameter to decorators  ( can be adj to include multple params)
# continued from 'decorators2
"""
# decorator w argument:
@decorator("foo")
def decorated_func():
    # function body....
    pass

# decorator w/o argument
@decorator
def other_decorated_func():
    #Function body
    pass
"""


from functools import wraps


def who_says(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if name.lower() == "simon":
                return func(*args, **kwargs)
            else:
                raise AttributeError("Simon didn't say")

        return wrapper

    return decorator


@who_says("Simon")
def add(a, b):
    return a + b


add(3, 5)  # runs ok as normal


@who_says("Bob")
def minus(a, b):
    return a - b


# minus(3, 5)  # raises Attribute errors


# OPTIONAL arguments
# method_or_options are parameters or option being wrapped


def gift(method_or_options=[]):
    def decorator(func):
        fields = []
        if not callable(method_or_options):
            fields = method_or_options

        @wraps(func)
        def wrapper(*args, **kwargs):
            if callable(method_or_options):
                print("Gift had no options")
            else:
                print("Gift had", fields)
            return func(*args, **kwargs)

        return wrapper

    # consider what happens if there are no parameters to @gift.
    #  In this case, there’s an extra layer of inner functions.
    #  You need to short circuit this inner layer. You can’t just return the closure, you have to invoke the closure.
    if callable(method_or_options):
        return decorator(method_or_options)

    return decorator


# no args
@gift
def add(a, b):
    return a + b


add(1, 2)

# with an option
@gift("ribbon")
def minus(a, b):
    return a - b


minus(3, 4)

# empty option
@gift()
def mult(a, b):
    return a * b


mult(5, 6)
