#!/usr/bin/python3
"""matrix-divided.

Divide every element of a given matrix by a specified number. The matrix must
be a list of lists.
"""


def matrix_divided(matrix, div):
    """Check if the matrix is valid and then divides each element by div."""
    if isinstance(matrix, list) is False:
        raise TypeError("""matrix must be a matrix (list of lists) of \
integers/floats""")
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError("""matrix must be a matrix (list of lists) of \
integers/floats""")
        for i in row:
            if isinstance(i, (int, float)) is False:
                raise TypeError("""matrix must be a matrix (list of lists) of \
integers/floats""")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div is 0 or div is 0.0:
        raise ZeroDivisionError("division by zero")
    div_mtx = []

    for row in matrix:
        div_mtx.append(list(map(lambda x: round(x / div, 2), row)))
    return div_mtx
