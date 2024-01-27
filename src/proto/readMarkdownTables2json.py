#!/usr/bin/env -S python -u
"""
"""

if __name__ == "__main__":

    snarfedFile = []

    with open("markdownFromTabli.md") as filePointer:
        snarfedFile = filePointer.readlines()

    for line in snarfedFile:
        print(line)

