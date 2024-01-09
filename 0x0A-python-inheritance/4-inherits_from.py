#!/usr/bin/python3
"""module if the object is an instance of a class that inherited (directly or indirectly"""

def inherits_from(obj, a_class):
    """determine if an object  is true of a class or no """
    return isinstance(obj, a_class) and type(obj) != a_class
