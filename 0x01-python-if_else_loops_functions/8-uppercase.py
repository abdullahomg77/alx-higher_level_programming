#!/usr/bin/python3
for i in "abc":
    if i >= 'a' and i <= 'z':
        i = ord(i) - 32
        print("{}".format(chr(i)), end="")
print()
