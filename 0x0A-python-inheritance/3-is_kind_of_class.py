#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """checks if `obj` is an instance of, or if the object is an
    instance of a class that inherited from , the specified class `a_class`"""
    return isinstance(obj, a_class)
