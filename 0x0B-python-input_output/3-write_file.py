#!/usr/bin/python3
"""Write to a file.
Write some text to a file. Creates a new one if it does not exist, overwrites
any previous content if it exists.
"""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        return my_file.write(text)
