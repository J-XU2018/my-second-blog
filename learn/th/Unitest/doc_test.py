"""
desc

"""

def sum(*args):
    """
    >>> sum(1, 2, 3)
    4

    """
    result = 0
    for i in args:
        result += i
    return result

# print(sum(1,2))
