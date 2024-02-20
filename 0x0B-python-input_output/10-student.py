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
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
