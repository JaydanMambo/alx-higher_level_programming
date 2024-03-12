#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('A') <= ord('str') <= ord('Z'):
            print("{:s}".format(char))
        else:
            print("{:s}".format(chr(ord(char) + 32)))
