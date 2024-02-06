#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        _type = isinstance(value, int)
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as VTE:
        print("Exception: {}".format(VTE), file=stderr)
    return False
