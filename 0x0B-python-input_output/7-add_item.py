#!/usr/bin/python3
"""the `add_item` module"""


import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

"""
load the file using try and except
if file doesnt exist, create empty list
extend the list and save to json
"""
try:
    items = load_from_json_file(filename)
except Exception:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
