#!/usr/bin/python3
"""the `Student` class module"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representaion of a Student instance"""
        return self.__dict__
