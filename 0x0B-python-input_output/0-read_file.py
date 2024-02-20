#!/usr/bin/python3

'''Read specific file'''


def read_file(filename=""):
    '''read file if exist, otherwise raise error'''
    if not filename:
        raise FileNotFoundError("file doesn't exist")
    with open(filename, 'r', encoding='utf-8') as file:
        stdout = file.read()
        print(stdout, end="")
