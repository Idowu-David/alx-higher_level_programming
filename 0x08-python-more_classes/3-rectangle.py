#!/usr/bin/python3
"""The `Rectangle` class module"""


class Rectangle:
    """Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the value of the Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width, with validations"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height, with validations"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of Rectangle"""
        rect = ""
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.height):
            rect += "#" * self.width
            if _ < self.height - 1:
                rect += "\n"
        return rect
