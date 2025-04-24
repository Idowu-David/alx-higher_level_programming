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
    flag = False
    for c in text:
        if c in chars:
            flag = True
        if flag and c == " ":
            flag = False
        else:
            if flag:
                print(c)
                print()
            else:
                print(c, end="")
