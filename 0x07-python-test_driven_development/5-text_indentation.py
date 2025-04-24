#!/usr/bin/python3
"""The `text_indentation` module provides a function that prints a text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after the characters `.`, `?` and `:`

    Args:
        text(str): the text to be printed.

    Raises:
        TypeError: if `text` is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ".?:"
    i = 0
    text_len = len(text)
    while i < text_len:
        print("{}".format(text[i]), end="")
        if text[i] in chars:
            print("\n")
            i += 1
            while i < text_len and text[i] == " ":
                i += 1
            continue
        i += 1
