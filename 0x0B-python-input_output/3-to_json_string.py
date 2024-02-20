#!/usr/bin/python3
'''Convert to json if can'''
from json import dumps


def to_json_string(my_obj):
    '''serialize `my_obj` to json
    if can!
    Returns:
    serialize obj to json with type string
    '''
    return dumps(my_obj)
