#!/usr/bin/python3
'''dict of variables of object'''

def class_to_json(obj: object):
    '''Return dict of obj'''
    return obj.__dict__
