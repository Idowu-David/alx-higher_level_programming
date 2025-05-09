#!/usr/bin/python3
"""the `BaseGeometry` module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """defines a Square geometry"""
    def __init__(self, size):
        """initializes the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
