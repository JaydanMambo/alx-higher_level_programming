#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_no = len(sys.argv) - 1
    if args_no == 0:
        print("{:d} arguements.".format(args_no))
    else:
        print("{:d}{}:".format(args_no, " arguement"
                               if args_no == 1 else " arguements"))
        for i in range(args_no):
            print("{:d}: {}".format(i + 1, sys.argv[i+1]))
