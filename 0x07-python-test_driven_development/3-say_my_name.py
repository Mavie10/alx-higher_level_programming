#!/usr/bin/python3
"""Module for say_my_name."""

def say_my_name(first_name, last_name=""):
    """method for printing first and last name.

    args:
        first_name: first name string
        last_name: last anme string
    
    Raises:
        TypeError: if first_name  or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.tetsfile("tests/3-say_my_name.txt")
