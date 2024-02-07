#!/usr/bin/python3

'''More upgrade for class square'''


class Square:
    "Hi I'm upgrade square"
    def __init__(self, size=0) -> None:
        '''Initialize square with size also with default value.

        Args:
            size (int): size of square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Return area of square'''
        return self.__size ** 2
