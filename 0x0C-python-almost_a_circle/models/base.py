#!/usr/bin/python3
"""Base class.
This class, which is going to be a parent class for other classes, keeps track
of each instance ID.
"""


import json


class Base:
    """Parent class. Keeps track of each class instance's ID."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of either Base or any other class."""
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list_dictionaries into a JSON string representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
