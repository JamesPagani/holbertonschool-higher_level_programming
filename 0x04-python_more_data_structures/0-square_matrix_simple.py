#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != [] and matrix is not None:
        sqr_mtx = []
        for i in range(len(matrix)):
            sqr_mtx.append(list(map(lambda n: n**2, matrix[i])))
        return sqr_mtx
