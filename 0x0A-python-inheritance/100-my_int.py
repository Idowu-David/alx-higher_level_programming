#!usr/bin/python3
"""`MyInt class"""


class MyInt(int):
    """defines a `int` rebel"""
    def __eq__(self, other):
        """invert == to !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """invert != to =="""
        return super().__eq__(other)
