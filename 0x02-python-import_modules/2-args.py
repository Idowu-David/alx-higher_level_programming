#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc < 1:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
