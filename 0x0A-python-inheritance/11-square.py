#!/usr/bin/python3
"""the `BaseGeometry` module"""


class BaseGeometry:
    """defines the BaseGeometry class"""
    def area(self):
        """calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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


class Square(Rectangle):
    """defines a Square geometry"""
    def __init__(self, size):
        """initializes the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the string representation of square"""
        return f"[Square] {self.__size}/{self.__size}"
