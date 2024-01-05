#!/usr/bin/python3
"""
Define a class rectangle
"""


class Rectangle:
    """representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
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
        """getter for private instance attribute height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return printable string representation of rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for _ in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def display(self):
        """display the rectangle with '#' characters"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __del__(self):
        """print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
