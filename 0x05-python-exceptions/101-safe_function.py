#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as E:
        print("Exception: {}".format(E), file=stderr)
    else:
        return res
