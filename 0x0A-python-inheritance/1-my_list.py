#!/usr/bin/python3
"""module for mylist"""

class Mylist(list):
    """custom Mylist class"""
    def print_sorted(Self):
        """method for print sorted list"""
        print(sorted(self))
