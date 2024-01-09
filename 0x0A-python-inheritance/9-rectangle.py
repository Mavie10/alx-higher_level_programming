#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        '''Method to calculate the area (to be overridden by subclasses)'''
        raise NotImplementedError("Subclasses must implement the area method")

    def perimeter(self):
        '''Method to calculate the perimeter (to be overridden by subclasses)'''
        raise NotImplementedError("Subclasses must implement the perimeter method")

    def integer_validator(self, name, value):
        '''Method to validate that a value is a positive integer.'''
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
