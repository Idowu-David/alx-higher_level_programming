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

    @property.setter
    def width(self, value):
        """sets the value of the width"""
        pass
