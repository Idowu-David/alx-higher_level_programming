#!/usr/bin/python3
"""The add_integer module"""


def add_integer(a, b=98):
    """adds two given integers

        Args:
            a(int): first integer
            b(int): second integer

        If a and b are first cased to integers if they're float
      """
    if type(a) not in (int, float) or a + 1 == a:
        raise TypeError("a must be an integer")
    if type(b) not in (int, float) or b + 1 == b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
