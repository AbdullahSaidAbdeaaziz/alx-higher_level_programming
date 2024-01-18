#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    number_args = len(argv) - 1
    if not number_args:
        print("{} arguments.".format(number_args))
    else:
        print("{} arguments:".format(number_args))
    for i, v in enumerate(argv[1:]):
        print("{}: {}".format(i+1, v))
