#!/usr/bin/python3
"""Square"""


class Square:
    """Define the Square"""

    def __init__(self, size=0):
        """Constructor: Set the size of the square."""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size  # Corrected the variable name

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
