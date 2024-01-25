#!/usr/bin/python3

def best_score(a_dictionary: dict):
    if not a_dictionary:
        return None
    max = -1
    key = None
    for k, v in a_dictionary.items():
        if v > max:
            max, key = k, v
    return key
