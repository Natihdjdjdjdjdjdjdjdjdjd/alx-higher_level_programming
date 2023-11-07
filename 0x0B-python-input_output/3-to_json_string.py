#!/usr/bin/python3
"""the function to_json_string"""
import json

def to_json_string(my_obj):
    """rjson representation of an object(string).

    Args:
        my_obj (type): represent string

    Returns:
        str: joson representation
    """
    return json.dumps(my_obj)
