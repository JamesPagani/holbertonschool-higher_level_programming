#!/usr/bin/python3
"""Number of lines.
Read a file and get the number of lines in it.
"""


def number_of_lines(filename=""):
    """Count the amount of lines in a file."""
    line_count = 0
    with open(filename, encoding="UTF-8") as my_file:
        for line in my_file:
            line_count += 1
    return line_count
