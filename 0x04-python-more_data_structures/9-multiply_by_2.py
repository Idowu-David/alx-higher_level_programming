#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = {}
    for k, v in a_dictionary.items():
        dic[k] = v * 2
    return dic
