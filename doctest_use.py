def fizz_buzz(numbers):
    """
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """
    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"


# usage:
# python3 -m doctest doctest_use.py


# use to exepect an error


class A:
    def error(self):
        """
        This function just errors
        >>> A().error
        Traceback (most recent call last):
        ...
        Exception: I am an error
        """
        raise Exception("I am an error")