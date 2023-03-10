7#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ string representation of square """
        print("[Square] {}/{}".format(self.__size, self.__size))
