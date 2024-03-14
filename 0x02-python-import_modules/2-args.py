#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_no = len(sys.argv) - 1
    if args_no == 0:
        print("{} arguments.".format(args_no))
    else:
        print("{}{}:".format(args_no, " arguement"
                             if args_no == 1 else " arguments"))
        for i in range(args_no):
            print("{:d}: {}".format(i + 1, sys.argv[i+1]))
