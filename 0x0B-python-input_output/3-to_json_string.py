#!/usr/bin/python3
"""the `to_json_string` module"""


import json


def to_json_string(my_obj):
    """returns the JSON representaion of an object (string)"""
    return json.dumps(my_obj)
