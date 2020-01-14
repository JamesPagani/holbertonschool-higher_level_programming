#!/usr/bin/python3
"""Say my name.

Recieve your first and last name and print them.

Both names have to be strings for this to work.
"""

def say_my_name(first_name, last_name=""):
    """Print your name."""
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
