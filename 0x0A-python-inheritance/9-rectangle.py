#!/usr/bin/python3
"""the `BaseGeometry` module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a Rectangle class"""
    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """returns the string representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
