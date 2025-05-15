#!/usr/bin/python3
"""the `Square` module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the Square instance"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the instance attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the value of square size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value for square size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns the string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
