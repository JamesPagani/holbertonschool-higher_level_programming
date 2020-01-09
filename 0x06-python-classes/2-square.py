#!/usr/bin/python3
"""Square class v2.

Instances a 'Square' class with:
    One integer attribute ('size').
"""


class Square:
    """Defines a Square with a size attribute."""

    def __init__(self, size=0):
            """Initialize an instance."""
            if isinstance(size, int) is False:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
