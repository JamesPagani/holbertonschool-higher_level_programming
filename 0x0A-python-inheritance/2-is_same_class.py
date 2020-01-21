#!/usr/bin/python3
"""Exact same object.

Write a function that returns True if the object is exactly an instance of the
specified class; Otherwise False.
"""


def is_same_class(obj, a_class):
    """Compare if obj is of the same type as a_class."""
    if type(obj) == a_class:
        return True
    else:
        return False
