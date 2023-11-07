#!/usr/bin/python3
"""
6-load_from_json_file module
"""
import json

def load_from_json_file(filename):
    """
    load_from_json_file - loads an object from JSON file.
        filename: name of the file is load of json
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
