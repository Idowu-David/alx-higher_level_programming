#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or sentence == "":
        s = None
    else:
        s = sentence[0]
    return (len(sentence), s)
