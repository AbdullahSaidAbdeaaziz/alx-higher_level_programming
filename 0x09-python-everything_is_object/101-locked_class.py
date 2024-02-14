#!/usr/bin/python3
'''Define LockedClass'''


class LockedClass:
    '''Prevent any attribute from creating except first_name'''

    __slots__ = ['first_name']
