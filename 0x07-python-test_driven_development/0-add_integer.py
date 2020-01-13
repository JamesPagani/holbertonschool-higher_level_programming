#!/usr/bin/python3
"""Integers addition.

This function adds two integers or floats. Returns the sum of both numbers.

If only one number is provided, the second will will default to 98.
"""


def add_integer(a, b=98):
    """Peform an addition of two numbers. Both have to be numbers."""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
