#!/usr/bin/python3
def islower(char):
    return char >= 97 and char <= 122


if __name__ == "__main__":
    for char in range(ord('a'), ord('z') + 1):
        if islower(char):
            print("{:c} is lower".format(char))
        else:
            print("{:c} is upper".format(char))
