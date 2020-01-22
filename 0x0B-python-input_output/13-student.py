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
        + reload_from_json(self, json): Replaces the values of all fields by
          the values in json (which is a dictionary)

Can update its values via JSON string/a new dictionary.
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
            if a in self.__dict__:
                out_dict[a] = self.__dict__.get(a)
        return out_dict

    def reload_from_json(self, json):
        """Load fields of this instance contained in a dictionary."""
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
