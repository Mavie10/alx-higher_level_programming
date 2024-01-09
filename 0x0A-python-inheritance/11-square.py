#!/usr/bin/python3
"""module for rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass representing a rectangle"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method for area of sqaure"""
        return self.__size ** 2

    def __str__(self):
        """return string of this square"""
        return "[square] " + str(self.__size) + "/" + str(self.__size)
