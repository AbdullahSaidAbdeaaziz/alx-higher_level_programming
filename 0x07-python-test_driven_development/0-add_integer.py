#!/usr/bin/python3

'''apply first task in using doctest to test function add_integer'''


def add_integer(a, b=98):
    '''
    add function
    Args:
        a (int or float): first number
        b (int or float, optional): second number

    Returns:
        int: sum of 2 number

    Raises:
        TypeError: if a or b is not integer or float
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
