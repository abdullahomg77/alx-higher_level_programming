#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if c == i:
            print("{} is lower".format(c))
            return True
        else:
            print("{} is upper".format(c))
            return False
