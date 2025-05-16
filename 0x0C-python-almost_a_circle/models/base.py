#!/usr/bin/python3
"""defines the `Base` class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
