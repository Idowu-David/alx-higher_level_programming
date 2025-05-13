#!/usr/bin/python3
"""the `Rectangle` module"""


from models.base import Base


class Rectangle(Base):
    """defines a Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of Rectangle instance"""
        return self.height * self.width

    def display(self):
        """prints the `Rectangle` instance with the character #"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """string representation of `Rectangle`"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
            {self.width}/{self.height}"
