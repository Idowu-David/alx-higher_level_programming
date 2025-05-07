#!/usr/bin/python3
"""the `BaseGeometry` module"""


class BaseGeometry:
    """defines the BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """defiens a Rectangle class"""
    def __init__(self, width, height):
        """initialization"""
        self.__width = width
        super().integer_validator(self.__width, width)
        self.__height = height
        super().integer_validator(self.__height, height)
