#!/usr/bin/python3
"""module for lookup method"""


def lookup(obj):
    """look up attribute
    args:
        obj: the object to list
    return:
        list: the list of the attribute
    """
    return dir(obj)
