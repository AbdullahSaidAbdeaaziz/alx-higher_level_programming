#!/usr/bin/python3
def remove(str, n):
    new_str = ""
    for i, v in enumerate(str):
        if i == n:
            continue
        new_str += v
