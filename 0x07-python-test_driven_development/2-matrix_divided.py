#!/usr/bin/python3
"""
The `matrix_divided` module provides a function to divide
all elements of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
   Divides all elements of a matrix by a given number

    Args:
        matrix(list of lists of int/float): The matrix to divide
        div(int or float): The divisor.add()

    Returns:
        list: A new matrix with elements divided and rounded to
        2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                    if each row is not the same size,
                    or if div is not a number
        ZeroDivisionError: If div is not zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div + 1 == div:
        raise TypeError("div must be a number")

    check_matrix(matrix)
    matrix2 = []
    for row in matrix:
        mat = []
        for ele in row:
            result = round(ele / div, 2)
            mat.append(result)
        matrix2.append(mat)
    return matrix2


def check_matrix(matrix):
    """
    Validates that the matrix is a proper list of equal-sized
    lists of ints/floats

    Args:
        matrix (list): The matrix to validate

    Raises:
        TypeError: If the matrix is invalid.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
