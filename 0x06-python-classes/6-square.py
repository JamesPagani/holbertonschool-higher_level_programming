#!/usr/bin/python3
"""Square class v4.

Instances a 'Square' class with:
    One integer attribute ('size').
    One Tuple attribute ('position')
        Size: 2
        Contents: (int, int)
    Two methods ('area' and 'my_print').

Unlike v5., v6.'s 'my_print' uses 'position' to move the square.
"""


class Square:
    """Defines a Square with a size attribute."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize an instance."""
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the square area of this square."""
        return self.__size ** 2

    def my_print(self):
        """Print a square."""
        if self.__size is 0:
            print()
        else:
            axis = self.__position
            for y in range(axis[1]):
                print()
            for i in range(self.__size):
                for x in range(axis[0]):
                        print(" ", end="")
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

    @property
    def position(self):
        """Get this square's position."""
        return self.__position

    @position.getter
    def position(sef, value):
        """Set this square's position."""
        if isinstance(value, tuple):
            print("position must be a tuple of 2 positive integers")
        elif not len(value) is 2:
            print("position must be a tuple of 2 positive integers")
        elif not type(tupl[0]) is int and not type(value[1]) is int:
            print("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
