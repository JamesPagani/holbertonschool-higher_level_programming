#!/usr/bin/python3
"""Read file.
Read an UTF-8 encoded file using open() and write each line to stdout.
"""


def read_file(filename=""):
    """Read and print the lines of a file."""
    with open(filename, encoding="UTF-8") as my_file:
        for line in my_file:
            print(line, end="")
