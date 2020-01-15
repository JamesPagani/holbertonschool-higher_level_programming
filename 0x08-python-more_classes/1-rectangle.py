#!/usr/bin/python3
"""Real definition of a rectangle (Rectangle v1).
Create a rectangle that contains the following attributes:
    width (integer, private).
    height (integer, private).
"""


class Rectangle:
    """Basic rectangle."""

    def __init__(self, width=0, height=0):
        """Initiate a basic rectangle."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve this rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set this rectangle's width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve this rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set this rectangle'sa height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
