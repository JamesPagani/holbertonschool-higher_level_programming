#!/usr/bin/python3
"""Only sub class of.

Write a function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """Check if obj is derivated from a_class."""
    obj_class = type(obj)
    if issubclass(obj_class, a_class) is True and obj_class is not a_class:
        return True
    else:
        return False
