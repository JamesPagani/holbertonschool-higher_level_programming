#!/usr/bin/python3
"""Area and perimeter (Rectangle v2).
Create a rectangle that contains the following attributes:
    FIELDS:
        width (integer, private).
        height (integer, private).
    METHODS:
        area (width * height, return an integer).
        preimeter (2 * (width + height), return an integer).
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

    def area(self):
        """Calculate the area of this rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of this rectangle."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
