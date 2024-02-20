#!/usr/bin/python3

'''Append to file'''


def write_file(filename='', text=''):
    '''
    Create file if not exist,
    and overwrite on content file with
    `text` parameter if exist there
    Returns:
    length of written in file
    '''
    if not filename:
        raise FileNotFoundError("file doesn't exist")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    written_in_file = len(text)
    return written_in_file
