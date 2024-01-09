#!/usr/bin/python3
"""Define the student class"""

import json


class Student:
    """Determine student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return JSON representation of the student"""
        return json.dumps(self.__dict__)

