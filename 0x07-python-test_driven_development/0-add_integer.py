#!/usr/bin/python3
"""Module of add_integer """

def add_integer(a, b=98):
    """Adding two integers togethers.

    Args:
    a: the first integer
    b : the second integer, default 98

    Raises:
        TypeError: if a, b are not int, float

    Returns:
        The sum of the two inetegers
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an ineteger')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_ineteger.txt")
