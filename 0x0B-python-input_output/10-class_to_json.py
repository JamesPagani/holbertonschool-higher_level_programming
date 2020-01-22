#!/usr/bin/python3
"""Class to JSON.
Save the dictionary description (__dict__) of a class as a JSON serialization.
"""


import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
