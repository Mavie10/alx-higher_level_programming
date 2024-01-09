#!/usr/bin/python3
"""define write file"""


def write_file(filename="", text=""):
    """read file with utf8"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
