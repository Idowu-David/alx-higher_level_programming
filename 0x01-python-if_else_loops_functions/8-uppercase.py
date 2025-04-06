#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if ord(let) >= 97 and ord(let) <= 123:
            lower = ord(let) - 32
        else:
            lower = ord(let)
        print("{}".format(chr(lower)), end="")
    print()
