#!/usr/bin/python3
"""module for same class method"""


def is_same_class(obj, a_class):
    """determine if an object is exact an isntance of a class or no"""
    return type(obj) == a_class
