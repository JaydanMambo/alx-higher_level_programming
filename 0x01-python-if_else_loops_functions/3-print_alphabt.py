#!/usr/bin/python3
for i in range(97, 123):
    if i not in (105, 113):
        print("{:c}".format(i), end='')
