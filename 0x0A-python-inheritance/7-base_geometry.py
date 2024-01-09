#!/usr/bin/python3
"""module for basegeometry class"""

class BaseGeometry:
    """basegeometry class"""
    def area(self):
        """method to compute area"""
        raise Exception('area() is not implemented')
    def integer_Validator(self, name, value):
        """method for validating the value"""
        if type(value) != int:
            raise TypeError("() must be an integer".format(name))
        if value <= 0:
            raise ValueError("() must be greater than 0".format(name))
