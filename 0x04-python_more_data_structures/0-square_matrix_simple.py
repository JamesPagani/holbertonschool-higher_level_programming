#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != [] and matrix is not None:
        sqr_pow = lambda n : n ** 2
        sqr_mtx = []
        for i in range(len(matrix)):
            sqr_mtx.append(list(map(sqr_pow, matrix[i])))
        return sqr_mtx
