#!/usr/bin/python3
"""My list.

Write a class MyList that inherits from list:
    METHODS:
        + print_sorted(self) - Prints the list, but sorted (does not modify
          original list)

Only tested with lists filled with integers.
"""


class MyList(list):
    """A class derived from the list built-in class."""

    def print_sorted(self):
        """Print a sorted list. Does not modify the original."""
        print(sorted(self))
