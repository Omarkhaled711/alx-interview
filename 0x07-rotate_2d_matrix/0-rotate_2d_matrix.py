#!/usr/bin/python3
"""
A module for rotating a 2d matrix problem
"""


def rotate_2d_matrix(matrix):
    """
    editing the 2d matrix in place
    """
    n = len(matrix[0])
    for i in range(n):
        for j in range(int(n/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = temp
    for i in range(n):
        for j in range(n - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][n - 1 - i]
            matrix[n - 1 - j][n - 1 - i] = temp
