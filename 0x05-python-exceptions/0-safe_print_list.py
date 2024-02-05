#!/usr/bin/python3

def _size(my_list):
    c = 0
    for i in my_list:
        c += 1
    return c


def safe_print_list(my_list=[], x=0):
    try:
        size = _size(my_list)
        if x > size:
            x = size
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except Exception:
        return size
