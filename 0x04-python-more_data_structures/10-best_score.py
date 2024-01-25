#!/usr/bin/python3

def best_score(a_dictionary: dict):
    if not a_dictionary:
        return None
    max = -1
    for v in a_dictionary.values():
        if v > max:
            max = v
    return max
