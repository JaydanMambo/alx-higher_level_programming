#!/usr/bin/python3
import sys
if __name__ == "__main__":
    av = sys.argv
    args_no = len(av) - 1
    if args_no == 0:
        print("{:d} arguments.".format(args_no))
    else:
        print("{:d}{}:".format(args_no, " arguement"
                               if args_no == 1 else " arguments"))
        for i in range(args_no):
            print("{:d}: {}".format(i + 1, av[i+1]))
