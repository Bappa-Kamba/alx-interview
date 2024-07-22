#!/usr/bin/python3
""" Module that ddefines a function to rotate a 2D matrix """


def rotate_2d_matrix(matrix):
    """
        Function that rotates a 2D matrix 90 degrees clockwise

        Args:
            matrix (list): 2D matrix to be rotated

        Returns:
            None
    """
    for i, row in enumerate(matrix):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        row.reverse()
