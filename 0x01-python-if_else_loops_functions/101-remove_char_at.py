#!/usr/bin/python3
def remove_char_at(str, n):
    dup = ""
    for i in range(len(str)):
        if i != n:
            dup += str[i]
    return dup
