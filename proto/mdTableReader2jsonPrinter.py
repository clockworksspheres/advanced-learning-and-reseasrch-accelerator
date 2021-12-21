#!/usr/bin/env -S python -u
"""
"""

import json
import re
import sys

def printSeparator():
    print("*****************************************************************")


def mdTable2json(mdString = ""):

    result = {}
    print(mdString)
    printSeparator()

    # for n, line in enumerate(mdString[1:-1].split('\n')):
    try:
        for line in mdString.split("\n"):
            data = {}
            line = line.strip()
            try:
                if re.match("^|", line):
                    line = line.strip("|")
                    zero, one = line.split("|")
                    #data[zero] = one
                    result[zero] = one
                    # if data[zero] not in result.keys():
                    #    result.append(data)
            except(ValueError):
                pass
    except(ValueError):
        pass
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inf = sys.argv[1]

        with open(inf, 'r') as f:
            s = f.read()
            print(s)
            jsonData = mdTable2json(s)
            print(jsonData)
            formattedJsonData = json.dumps(jsonData, indent=3)
            print(formattedJsonData)





