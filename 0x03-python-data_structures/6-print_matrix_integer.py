#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for i, col in enumerate(row):
            print("{:d}".format(col), end='')
            if i != len(row) - 1:
                print(end=" ")
        print()
