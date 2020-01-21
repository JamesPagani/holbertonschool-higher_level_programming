#!/usr/bin/python3
"""Read n lines.
Read and print at most n amount of lines of a file.
"""


def read_lines(filename="", nb_lines=0):
    """Read at most nb_lines amount of lines."""
    with open(filename, encoding="UTF-8") as my_file:
        line_count = 0
        for line in my_file:
            print(line, end="")
            line_count += 1
            if line_count == nb_lines:
                break
