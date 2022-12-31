#!/usr/bin/env -S python -u
"""
"""

import json
import re
import sys

import click

def printSeparator():
    print("*****************************************************************")


def mdTable2baseJsonDict(mdString = ""):
    """
    uses a uniq type approach to not get any duplicate entries.. not good for 
    accessing collections per webpage... Operates on a passed in string, creates
    a dictionary from table entries, and returns that.
    """

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

@click.command()
@click.option("-f", "--filename", type=str, help="Markdown filename to load")
@click.option("-v", "--verbose", is_flag=True, help="Print more output.")
def parse_args(filename, verbose):
    """ Parse .md table for link and description key - value pairs """
    click.echo(f"filename: {filename}")
    click.echo(f"verbose flag: {verbose}")
    return {"filename": filename, "verbose": verbose}

if __name__ == '__main__':
    arguments = parse_args()

    # if len(sys.argv) > 1:
    #    inf = sys.argv[1]
    # with open(inf, 'r') as f:
    with open(arguments["filename"], 'r') as f:
        s = f.read()
        print(s)
        jsonData = mdTable2baseJsonDict(s)
        print(jsonData)
        formattedJsonData = json.dumps(jsonData, indent=4)
        print(formattedJsonData)
