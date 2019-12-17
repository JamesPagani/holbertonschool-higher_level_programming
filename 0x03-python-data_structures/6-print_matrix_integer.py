#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        delim = ""
        for j in matrix[i]:
            print(delim, j, sep="", end="")
            delim = " "
        print("")
