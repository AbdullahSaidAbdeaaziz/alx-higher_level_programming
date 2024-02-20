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

    def to_json(self, attrs=None):
        '''
        Reterive dict of attributes in class Student
        Args:
        attrs (optional, list[string])
        Return  dictionary representation of a Student'''
        if not attrs:
            return self.__dict__
        new_dict = {}
        for attr in attrs:
            for key in self.__dict__:
                if key == attr and isinstance(attr, str):
                    new_dict.update({key: self.__dict__[key]})
                    break
        return new_dict
