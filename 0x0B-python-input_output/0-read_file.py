#!/usr/bin/python3
"""define read_File"""


def read_file(filename=""):
    """read filename with utf8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
