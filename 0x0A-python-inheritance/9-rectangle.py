#!/usr/bin/python3
"""Module for rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """a subclass representing a rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method which returns area of rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """string representation """
        return "[rectangle] " + str(self.__height)