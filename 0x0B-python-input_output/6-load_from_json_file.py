#!/usr/bin/python3
"""the `load_from_json_file` module"""


import json


def load_from_json_file(filename):
    """creates an Object from a `JSON file`"""
    with open(filename, 'r', encoding='utf-8') as f:
        fp = f.read()
    return json.loads(fp)
