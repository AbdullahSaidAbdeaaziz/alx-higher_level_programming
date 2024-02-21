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
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''
        Replaces all attributes of the Student instance
        Args:
        json (dict): json file
        '''
        for k, v in json.items():
            self.__dict__[k] = v
