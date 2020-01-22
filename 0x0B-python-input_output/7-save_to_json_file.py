#!/usr/bin/python3
"""Save Object to file.
Save a JSON string representation of a Python object in a file.
"""


import json


def save_to_json_file(my_obj, filename):
    """Write to a file a JSON string of my_object."""
    with open(filename, mode="w") as json_file:
        json_file.write(json.dumps(my_obj))
