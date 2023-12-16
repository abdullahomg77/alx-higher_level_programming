#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    t = 0
    number = 0
    digit = {'I': 1, 'V': 5 , 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roman_string):
        number = digit[i]
        t += number if t < number * 5 else -number
    return t

