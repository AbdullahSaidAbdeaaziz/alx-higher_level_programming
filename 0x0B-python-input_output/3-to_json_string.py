#!/usr/bin/python3
from json import dumps
'''Convert to json if can'''


def to_json_string(my_obj):
    '''serialize my_obj to json
    if can!
    '''
    return f'{dumps(my_obj)}'
