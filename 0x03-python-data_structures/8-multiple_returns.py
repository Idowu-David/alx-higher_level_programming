#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or sentence == "":
        sentence[0] = None
    return (len(sentence), sentence[0])
