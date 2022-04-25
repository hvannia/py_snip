# walrus in list comprehen
# simulate 'slow' function, which is called twice per number

import time


def slow(mum):
    time.sleep(1)
    return num


numbers = [7, 6, 1, 4, 1, 8, 0, 6]
results = [slow(num) for num in numbers if slow(num) > 0]

# a possible solution : a for loop or  a double list comprehension - hard to read

results = [value for num in numbers for value in [slow(num)] if value > 0]

# or better yet walrsu

results = [value for num in numbers if (value := slow(num)) > 0]


# other example from reralpython
# ( code in folder )
# https://realpython.com/lessons/assignment-expression-pass-by-reference/

# try_parse3.py
def try_parse(string, base=10):
    try:
        return int(string, base=base)
    except ValueError:
        return None


values = ["", "160519", "9432.0", "16,667", "   -322   ", "+4302", "(100);", "01FA"]

for value in values:
    if (number := try_parse(value)) is not None:
        print(f"Converted {value} to {number}")
    else:
        print(f"Attempted conversion of {value} failed")
