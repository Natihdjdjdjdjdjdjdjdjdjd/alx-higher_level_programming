#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = matrix.copy()

    for x in range(len(matrix)):
        square_matrix[x] = list(map(lambda y: y**2, matrix[x]))

        return (square_matrix)
