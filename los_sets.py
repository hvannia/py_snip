# count unique characters in s
# example 1 - w/o sets


def count_unique(s):
    """
    Count the number of unique characters in s
    >>> count_unique("aabb")
    2
    >>> count_unique("abcdef")
    6
    """
    # seen_char = []  # O(1)
    # for c in s:  # O(n)
    #     if c not in seen_char:  # O(n)
    #         seen_char.append(c)  # O(1)
    # return len(seen_char)  # O(n^2)

    # checking for existstance of a value in a set is alway O(1)
    # seen_char = set()  # O(1)
    # for c in s:  # O(n)
    #     if c not in seen_char:  # O (1)
    #         seen_char.add(c)  # O (1)
    # return len(seen_char)  # O(n)

    # set comprehension
    # return len({c for c in s})  # O(n)
    # or
    return len(set(s))
