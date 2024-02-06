#!/usr/bin/python3
from __future__ import print_function
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(args)
    except Exception as E:
        print("Excetion: {}".format(E), file=stderr)
    else:
        return res
