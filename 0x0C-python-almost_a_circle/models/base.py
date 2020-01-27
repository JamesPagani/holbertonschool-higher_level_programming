#!/usr/bin/python3
"""Base class.
This class, which is going to be a parent class for other classes, keeps track
of each instance ID.
"""


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
