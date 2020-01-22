#!/usr/bin/python3
"""Pascal Triangle.
A function that builds a Pascal Triangle of a given height/depth.
"""


def pascal_triangle(n):
    triangle = []
    prev = []
    curr = []

    for i in range(1, n + 1):
        prev = curr[:]
        curr.clear()
        for j in range(i):
            if j == 0 or j + 1 == i:
                curr.append(1)
            else:
                curr.append(prev[j] + prev[j - 1])
        triangle.append(list(curr))
    return triangle
