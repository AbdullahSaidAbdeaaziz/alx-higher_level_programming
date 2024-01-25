#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight = 0
    average = 0
    for f, s in my_list:
        average += s
        weight += f * s
    return weight / average
