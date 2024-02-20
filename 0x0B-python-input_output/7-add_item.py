#!/usr/bin/python3
'''adds all arguments to a Python list,
and then save them to a file
'''
from sys import argv


def main():
    '''adding all args to file, load it again and add it file'''
    load_file = __import__('6-load_from_json_file').load_from_json_file
    save_file = __import__('5-save_to_json_file').save_to_json_file
    
    try:
        items = load_file('add_item.json')
    except Exception:
        items = []
    items += argv[1:]
    save_file(items, 'add_item.json')


if __name__ == '__main__':
    main()
