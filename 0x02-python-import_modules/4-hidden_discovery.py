#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def_names = hidden_4.__dict__
    for name in def_names:
        if name[:2] != '__':
            print(name)
