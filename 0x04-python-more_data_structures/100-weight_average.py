#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    av = 0
    for lis in my_list:
        mul = lis[0] * lis[1]
        av += lis[1]
        sum += mul
    return sum / av
