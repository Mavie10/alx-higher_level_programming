#!/usr/bin/python3
"""Define the student class"""


class Student:
    """Determine student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the student"""
        return self.__dict__
