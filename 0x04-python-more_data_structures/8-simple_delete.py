#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if not a_dictionary.get(key, None):
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
