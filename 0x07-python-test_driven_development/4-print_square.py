#!/usr/bin/python3
"""Print square.

Print a square of user-given size, as long as the size is a positive integer.
"""

def print_square(size):
    """Print a square of size 'size'."""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size is 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
