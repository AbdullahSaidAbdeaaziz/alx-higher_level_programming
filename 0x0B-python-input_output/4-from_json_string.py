#!/usr/bin/python3
'''convert json string to object like dict, list..etc'''
from json import loads


def from_json_string(my_str):
    '''Returns DS of json `my_str`'''
    return loads(my_str)