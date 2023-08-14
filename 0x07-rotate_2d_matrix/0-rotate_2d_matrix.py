#!/usr/bin/python3
"""
Rotating a 2D matrix clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate a 2D matrix

    Args: matrix

    Returns: nothing
    """
    matrix[:] = [list(row[::-1]) for row in zip(*matrix)]
