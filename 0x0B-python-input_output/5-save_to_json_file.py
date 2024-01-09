#!/usr/bin/python3
"""define save json"""

import json

def save_to_json_file(my_obj, filename):
    """write an obj to txt file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
