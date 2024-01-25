#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matix = [
        list(map(lambda x: x**2, m)) for m in matrix
        ]
    return new_matix
