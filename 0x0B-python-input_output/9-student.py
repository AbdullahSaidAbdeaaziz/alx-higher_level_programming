#!/usr/bin/python3
'''Create class Student'''


class Student:
    '''made class student'''
    def __init__(self, first_name, last_name, age) -> None:
        '''Initialize first_name
        last_name, age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Return  dictionary representation of a Student'''
        return self.__dict__
