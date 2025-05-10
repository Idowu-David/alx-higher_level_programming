#!/usr/bin/python3
"""the `append_after` modulef"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string
    """
    with open(filename, 'r') as f:
        texts = f.readlines()
    with open(filename, 'w') as f:
        for text in texts: 
            if search_string in text:
                f.write(text)
                f.write(new_string)
            else:
                f.write(text)
