#!/usr/bin/python3
"""
This module defines the Square class for basic geometric calculations.add()

Classes:
    Square: Represents a square
"""


class Square:
    """
    Represents a geometric square.

    Attributes:
        size (int): The length of one side of the square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
