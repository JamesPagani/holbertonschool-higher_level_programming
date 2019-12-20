#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mtx = []
    for i in matrix:
        sqr_mtx.append(list(map(lambda n: n ** 2, i)))
    return sqr_mtx
