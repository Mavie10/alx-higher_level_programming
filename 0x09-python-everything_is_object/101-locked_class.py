#!/usr/bin/python3
"""Define a locked class"""



class LockedClass:
    """
    Prevent user from instantiating
    """

    __slots__ = ("first_name")
