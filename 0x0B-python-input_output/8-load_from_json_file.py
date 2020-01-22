#!/usr/bin/python3
"""Create object from a JSON file.
Create a Python object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """Create an object from a .json file."""
    with open(filename, mode="r") as json_file:
        json.loads(json_file.read())
