#!/usr/bin/python3
"""Same class or inherit from.

Write a function that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from, the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or derived from a_class."""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
