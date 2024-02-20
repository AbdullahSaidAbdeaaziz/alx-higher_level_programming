#!/usr/bin/python3
'''Save json in file'''
from json import dumps


def save_to_json_file(my_obj, filename):
    '''save object in json form in json file'''
    with open(filename, 'w') as json:
        json.write(dumps(my_obj))
