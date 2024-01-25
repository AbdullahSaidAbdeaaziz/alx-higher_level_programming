#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    if len(roman_string) == 1:
        return roman_int[roman_string[0]]
    number = 0
    i = 0
    # ICI
    while i < len(roman_string):
        first = roman_int[roman_string[i]]
        if i + 1 < len(roman_string):
            next = roman_int[roman_string[i + 1]]
        else:
            next = -1
        if next > first:
            number += (next - first)
            i += 2
            continue
        number += first
        i += 1
    return number
