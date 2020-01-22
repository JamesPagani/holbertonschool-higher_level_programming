#!/usr/bin/python3
"""Class to JSON.
Save the dictionary description (__dict__) of a class to be used in
JSON serialization.
"""


def class_to_json(obj):
    """Serialize the directory description of a class into JSON."""
    return obj.__dict__
