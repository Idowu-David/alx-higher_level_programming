#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    ind = len(roman_string) - 1
    sum = 0
    i = 0
    flag = 0
    while i < ind:
        if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            sum += roman_dict[roman_string[i]]
        else:
            op = roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
            sum += op
            i += 2
            flag = 1
        if flag != 1:
            i += 1
    if i <= ind:
        sum += roman_dict[roman_string[i]]
    return sum
