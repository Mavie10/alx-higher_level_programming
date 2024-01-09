#!/usr/bin/python3
"""define load json"""

import json


def load_from_json_file(filename):
    """create obj from json"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
