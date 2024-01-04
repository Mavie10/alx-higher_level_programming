#!/usr/bin/python3
"""
Define a class rectangle
"""

class rectangle:
    """representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(Self):
        """getter for private instance attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private isntance attribute height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value is not int:
                raise TypeError("height must be an integer")
        if value < 0;
                raise ValueError("height must be >= 0")
        self.__height = value
