#!/usr/bin/python3
"""Append to file.
Write more text to a file. Creates it if it does not exist.
"""


def append_write(filename="", text=""):
    """Append text to a file and return the amount of characters written."""
    with open(filename, mode="a", encoding="UTF-8") as my_file:
        return my_file.write(text)
