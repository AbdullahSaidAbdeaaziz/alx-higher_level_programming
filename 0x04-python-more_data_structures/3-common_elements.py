#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = set_1 & set_2
    convert_list = list(common_set)
    return convert_list
