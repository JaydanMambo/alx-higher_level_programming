#!/usr/bin/python3
def uppercase(str):
    if ord('A') <= ord('str') <= ord('Z'):
        print("{:s}".format(str))
    else:
        print("{:s}".format(chr(ord(str) + 32)))
