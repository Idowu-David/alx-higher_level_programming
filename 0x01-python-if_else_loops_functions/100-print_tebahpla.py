#!/usr/bin/python3
for i in range(26, 52, 2):
    print("{}{}".format(chr(148 - i), chr(115 - i)), end="")