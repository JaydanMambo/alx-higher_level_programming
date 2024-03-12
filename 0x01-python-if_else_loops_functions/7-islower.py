#!/usr/bin/python3
def islower(char):
    return char >= 97 and char <= 122


if __name__ == "__main__":
    for char in range(ord('a'), ord('z') + 1):
        if islower(char):
            print("{} is lower".format(char))
        else:
            print("{} is upper".format(char))
