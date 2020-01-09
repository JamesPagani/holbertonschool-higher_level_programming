#!/usr/bin/python3
"""Square class v4.

Instances a 'Square' class with:
    One integer attribute ('size').
    Two methods ('area' and 'my_print').
"""


class Square:
    """Defines a Square with a size attribute."""

    def __init__(self, size=0):
        """Initialize an instance."""
        self.__size = size

    def area(self):
        """Calculate the square area of this square."""
        return self.__size ** 2

    def my_print(self):
        """Print a square."""
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

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
