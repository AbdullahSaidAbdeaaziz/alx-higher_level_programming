#!/usr/bin/python3

'''More upgrade for class square'''


class Square:
    "Hi I'm upgrade square"
    def __init__(self, size=0, position=(0, 0)) -> None:
        '''Initialize square with size also with default value.

        Args:
            size (int): size of square
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''get size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set value to size of square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''get coordinate of square'''
        return self.__position

    @position.setter
    def position(self, coordinate):
        '''set coordinate of square'''
        if (not isinstance(coordinate, tuple) or
                len(coordinate) != 2 or
                not all(isinstance(num, int) for num in coordinate) or
                not all(num >= 0 for num in coordinate)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = coordinate

    def area(self):
        '''Return area of square'''
        return self.__size ** 2

    def my_print(self):
        '''print shape of square'''
        if not self.__size:
            print("")
            return
        print(""*self.position[1])
        for _ in range(self.__size):
            print(f'{" "*self.__position[0]}{"#"*self.__size}')
