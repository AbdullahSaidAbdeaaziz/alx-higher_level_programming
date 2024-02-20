#!/usr/bin/python3
'''load object contains json from file'''
from json import load


def load_from_json_file(my_obj, filename):
    '''put json file in object to deal it later'''
    with open(filename) as json_file:
        return load(json_file)
