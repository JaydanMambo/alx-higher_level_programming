#!/usr/bin/python3
def remove_char_at(input_str, n):
    result_str = ""
    for i in range(len(input_str)):
        if i != n:
            result_str += input_str[i]
    return result_str
