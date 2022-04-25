import os
from logzero import logger

# clear (empty) a file if exists
def clearf(filename):
    if os.path.isfile(filename):
        with open(filename, "r+") as f:
            f.truncate(0)
    logger.info(f"cleared {filename}")


def append_tofile(filename, l, newline=True):
    with open(filename, "a") as f:
        if newline:
            f.write(l + "\n")
        else:
            f.write(l)


def count_lines_file(filename):
    print(f"{len(open(filename).readlines( ))} lines in {filename}")


# check for file access
import os

os.access("./text.txt", os.R_OK)
os.access("./text.txt", os.W_OK)
os.access("./text.txt", os.X_OK)


# zip
import zipfile

with zipfile.Zipfile("spam.zip") as myzip:
    with myzip.open("eggs.txt") as myfile:
        print(myfile.read())
