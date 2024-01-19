#  initial context manager


class PrintingContextManager:
    def __enter__(self):
        print("entering the context manager")
        return "i am the returned value"

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting the context manager")


with PrintingContextManager() as var:
    print("inside the context manager")
    print(var)


# rewrite this context manager in a more consise way though by using a generator and a decorator.
from contextlib import contextmanager


@contextmanager
def printing_context_manager():
    print("entering the context manager")
    yield "i am the returned value"
    print("exiting the context manager")


with printing_context_manager() as var:
    print("inside the context manager")
    print(var)


# UTILITIES

with open("file.txt") as f:
    lines = f.read()

lines.split("\n")


# setup and teardown temp file
import tempfile

with tempfile.TemporaryDirectory() as tempdir_path:
    print(f"I have a temporary directory at: {tempdir_path}")

with tempfile.TemporaryFile(mode="w+") as file:
    file.write("hello, world")
    file.seek(0)
    print(file.readlines())


## Redirect
# redirect the default target of print (stdout), to some other place, like an io.StringIO() object.
# This is a great use-case for a context manager:

import io
from contextlib import redirect_stdout

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)

regr = RandomForestRegressor(
    max_depth=2,
    n_estimators=5,
    random_state=0,
    verbose=100,  # <---------- this is what makes sklearn print
)

with redirect_stdout(io.StringIO()) as f:
    regr.fit(X, y)


# You can now access the printed output via
print(f.get_value())


# ENV variables
# writing unit tests that deal with environment variables:
from contextlib import contextmanager
import os


@contextmanager
def set_env_vars(**kwargs):
    # Remember old values
    previous_values = {k: os.environ[k] for k in kwargs if os.environ.get(k, None)}
    # Set new values
    for k, v in kwargs.items():
        os.environ[k] = v
    yield
    # Put everything back into place
    for k, v in previous_values.items():
        os.environ[k] = v


with set_env_vars(APP_KEY="something-else"):
    print(os.environ["APP_KEY"])
print(os.environ["APP_KEY"])
