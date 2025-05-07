#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """checks if the `obj` is exactly an instane of the `a_class`"""
    return type(obj) is a_class
