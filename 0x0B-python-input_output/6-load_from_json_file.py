#!/usr/bin/python3
'''load object contains json from file'''
from json import loads


def load_from_json_file(my_obj, filename):
    '''put json file in object to deal it later'''
    with open(filename, 'r') as json_file:
        content = json_file.read()
    return loads(content)
