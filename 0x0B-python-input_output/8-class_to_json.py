#!/usr/bin/python3
"""define class json"""


def class_to_json(obj):
    """return dic with simple data
    (list, dictionary, string, integer and boolean)
    for json """
    return obj.__dict__
