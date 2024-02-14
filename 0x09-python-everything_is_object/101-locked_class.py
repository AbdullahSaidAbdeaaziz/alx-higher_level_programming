#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, __name, __value):
        if __name == 'last_name':
            raise AttributeError("'LockedClass' has no attribute 'last_name'")
