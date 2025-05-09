#!/usr/bin/python3
"""the `write_file` module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    
    Return: the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
