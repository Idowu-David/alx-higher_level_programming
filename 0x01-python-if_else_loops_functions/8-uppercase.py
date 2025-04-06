#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if ord(let) >= 97 and ord(let) <= 123:
            print("{}".format(chr(ord(let) - 32)), end="")
        else:
            print("{}".format(let), end="")
    print()
