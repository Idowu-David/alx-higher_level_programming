#!/usr/bin/python3
"""The `locked_class` module"""


class LockedClass:
    """
    This class prevents the user from dynamically creating
    new instance attributes, except if it is called `first_name`
    """
    __slots__ = ('first_name',)
