#!/usr/bin/python3
"""Geometry module.

A parent class with the following attributes:
    METHODS:
        + area(self): Raises an Exception (not implemented yet).
        + integer_validator(self, name, value): Validates if value is an int.

Can only check if the value given in integer_validator is a int or not.
"""


class BaseGeometry:
    """Has a method, but it is not implemented, so it raises an exception."""

    def area(self):
        """Not implemented yet. DO NOT USE."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
