#!/usr/bin/python3
"""
The `print_square` module provides a that prints a square with the character #
"""


def print_square(size):
    """
   Prints a square with the character #

    Args:
        size(int): the size length of the square.

    Raises:
        TypeError: If the size is not an integer.
                    or if the size is a float less than 0
         ValueError: if the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for _ in range(size):
            print("#" * size)
