#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for c in str:
        if not c.islower():
            upper_str += c
            continue
        upper_char = ord(c) - 32
        upper_str += chr(upper_char)
    print(upper_str)
