#!/usr/bin/python3
"""defines the `Base` class"""


class Base:
    """
    Base class for managing id attributes across all future classes.

    Attributes:
        __nb_objects (int): A class-level counter to assign unique IDs.
        id (int): The identity of the instance, set manually or automatically
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base instances"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
