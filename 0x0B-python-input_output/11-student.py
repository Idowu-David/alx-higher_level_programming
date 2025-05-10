#!/usr/bin/python3
"""the `Student` class module"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representaion of a Student instance"""
        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__
    
    def reload_from_json(self, json):
        """replaces all attributes of the `Student` instance"""
        for key, value in json.items():
            setattr(self, key, value)
