#!/usr/bin/python3
"""define append write function"""


def append_write(filename="", text=""):
    """append filename with utf8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
