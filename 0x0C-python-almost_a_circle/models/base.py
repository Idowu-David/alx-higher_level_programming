#!/usr/bin/python3
"""defines the `Base` class"""


import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs
        to a file

        Argument:
            list_objs(list): a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            json_str = "[]"
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(list_dicts)
        with open(filename, 'w') as fp:
            fp.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of JSON string representation

        Arguments:
            json_string: a string representing a list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as fp:
                json_str = fp.read()
            json_list = cls.from_json_string(json_str)
            return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes objects in CSV"""
        filename = cls.__name__ + ".json"
        field = ("id", "size", "x", "y") if cls.__name__ == "Square" \
            else ("id", "width", "height", "x", "y")
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=field)
            for obj in (list_objs or []):
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes objects in CSV"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.DictReader(f)
                objs = [cls.create(**{k: int(v) for k, v in row.items()})
                        for row in reader]
            return objs
        except FileNotFoundError:
            return []
