#!/usr/bin/python3
"""
========================================
Module for matrix_divied
========================================
"""


def matrix_divided(matrix, div):
"""Function matix divided"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [i[:] for i in matrix]
    rows = len(matrix[0])
