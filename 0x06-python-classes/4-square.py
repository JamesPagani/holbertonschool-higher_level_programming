#!/usr/bin/python3
"""Square class v4.

Instances a 'Square' class with:
    One integer attribute ('size').
    One method ('area').

Unlike v3., this version now comes with the getters and setters.
"""


class Square:
    """Defines a Square with a size attribute."""

    def __init__(self, size=0):
        """Initialize an instance."""
        self.__size = size

    def area(self):
        """Calculate the square area of this square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get this square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set this square's size."""
        if isinstance(value, int) is False:
                raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = value
