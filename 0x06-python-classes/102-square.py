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
        self.size = size

    @property
    def size(self):
        """Gets the size of the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size after validations"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compares two squares for equality based on their size"""
        return self.size == other.size

    def __ne__(self, other):
        """Compares two squares for inequality based on their size"""
        return self.size != other.size

    def __gt__(self, other):
        """Compares to check if a square is greater than the other"""
        return self.size > other.size

    def __lt__(self, other):
        """Compares to check if a suqare is less than the other"""
        return self.size < other.size

    def __ge__(self, other):
        """
        Compares to check if a square is greater than or equal to the other
        """
        return self.size >= other.size

    def __le__(self, other):
        """Compares to check if a square is less than or equal to the other"""
        return self.size <= other.size
