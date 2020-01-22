#!/usr/bin/python3
"""Student to JSON.
A Student class with the folowing attributes:
    FIELDS:
        + first_name (Instance, Public)
        + last_name (Instance, Public)
        + age (Instance, Public)
    METHODS:
        + __init__(self, first_name, last_name, age): Init method
        + to_json(self): Retrieves a dictionary description of a Student
          instance (in JSON serialization)

A basic class with JSON Serialization implementation.
"""


class Student:
    """A Student at Holberton School."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
