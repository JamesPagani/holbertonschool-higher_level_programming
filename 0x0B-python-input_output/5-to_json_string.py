#!/usr/bin/python3
"""To JSON string.
A function that returns the JSON string representation of a Python object.
"""


import json


def to_json_string(my_obj):
    """Return a JSON representation of my_obj."""
    return json.dumps(my_obj)
