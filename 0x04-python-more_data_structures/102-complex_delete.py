#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    new_dict = {}
    for k, v in a_dictionary.items():
        if v != value:
            new_dict[k] = v
    a_dictionary = new_dict
    return a_dictionary
