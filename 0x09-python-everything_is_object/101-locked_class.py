#!/usr/bin/python3
'''Define LockedClass'''


class LockedClass:
    '''Prevent last_name attribute from creating'''

    def __setattr__(self, __name, __value):
        '''
        check instance name of attribute that begin pass to class
        Raises:
        AttributeError: class has no attribute last_name
        '''

        if f'__{__name}' in self.__dict__.keys():
            raise AttributeError("'LockedClass' has no attribute 'last_name'")
