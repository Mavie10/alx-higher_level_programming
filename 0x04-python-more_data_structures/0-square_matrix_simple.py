#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    return list(map(lambda submatrix: list(map(lambda i: i**2, submatrix)), matrix)
