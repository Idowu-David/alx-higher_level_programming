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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if (type(value) is not tuple or len(value) != 2 or
            not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
