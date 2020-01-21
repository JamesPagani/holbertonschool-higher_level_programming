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
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A geometric figure: The rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        self.__height = height
        self.__width = width

    def __str__(self):
        """Information of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """A rectangle with equal width and height."""

    def __init__(self, size):
        """Initialize a new Square."""
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
