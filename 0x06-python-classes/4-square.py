#!/usr/bin/python3
"""Square"""


class Square:
    """Define the Square"""

    def __init__(self, size=0):
        """Constructor: Set the size of the square."""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
