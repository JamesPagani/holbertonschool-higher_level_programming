#!/usr/bin/python3
"""Lookup.

Write a function that returns the list of all available attributes and methods
of an object.

Returns a list object.
"""


def lookup(obj):
    """Return the contents of an object."""
    return dir(obj)
