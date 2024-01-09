#!/usr/bin/python3
"""add attribute"""

class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initialize object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation attribute"""
        try:
            if attrs is not None:
                for attr in attrs:
                    if type(attr) is not str:
                        return self.__dict__
        except Exception:
            return self.__dict__
        
        my_dict = dict()
        for key, value in self.__dict__.items():
            if attrs is None or key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """replace the student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value

