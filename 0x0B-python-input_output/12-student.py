#!/usr/bin/python3
"""Student to JSON.
A Student class with the folowing attributes:
    FIELDS:
        + first_name (Instance, Public)
        + last_name (Instance, Public)
        + age (Instance, Public)
    METHODS:
        + __init__(self, first_name, last_name, age): Init method
        + to_json(self, attrs=None): Retrieves a dictionary description of a
          Student instance.
            - If attrs is a list of strings, the dictionary will contain only
              the fields listed in in attrs.
            - Otherwise, the dictionary will contain all fields.

Upgraded to_json method: May return specific attribute(s).
"""


class Student:
    """A Student at Holberton School."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve this instance's dictionary description."""
        if not type(attrs) is list:
            return self.__dict__
        for a in attrs:
            if not type(a) is str:
                return self.__dict__

        out_dict = {}
        for a in attrs:
            out_dict[a] = self.__dict__.get(a)
        return out_dict
