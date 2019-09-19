#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = [list(map(lambda i: i ** 2, j)) for j in matrix]
        return new_matrix
