#!/usr/bin/python3
"""the `print_sorted` module"""


class MyList(list):
    """defines a class that inherits from list obj"""
    def print_sorted(self):
        """prints the list but sorted(ascending order)"""
        print(sorted(self))
