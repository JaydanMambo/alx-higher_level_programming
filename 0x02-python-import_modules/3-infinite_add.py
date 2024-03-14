#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    arg_no = len(sys.argv) - 1
    for i in range(arg_no):
        sum = sum + int(sys.argv[i + 1])
    print(sum)
