#!/usr/bin/env -S python -u
"""
"""

import json
import re
import sys
import configparser
import click
# import typer


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


"""
Fuzzy Search Stuff:
https://reposhub.com/cpp/miscellaneous/maxbachmann-rapidfuzz.html
https://pythonawesome.com/rapid-fuzzy-string-matching-in-python-using-various-string-metrics/
https://www.youtube.com/watch?v=SoZ1CVU2DdE
https://www.google.com/search?client=firefox-b-1-d&q=github+rapidfuzz
https://github.com/maxbachmann/RapidFuzz
https://maxbachmann.github.io/RapidFuzz/
https://medium.com/mlearning-ai/all-about-rapidfuzz-string-similarity-and-matching-cd26fdc963d8
https://www.libhunt.com/r/RapidFuzz
https://www.linkedin.com/pulse/all-fuzzyness-python-zhuoyi-zhao
"""

"""
command line options
argparse : std python lib : https://docs.python.org/3/howto/argparse.html 
click: : BSD 3 clause : https://github.com/pallets/click
typer: MIT : https://github.com/tiangolo/typer
https://typer.tiangolo.com/tutorial/using-click/
https://typer.tiangolo.com/
https://realpython.com/python-typer-cli/
https://towardsdatascience.com/typer-build-powerful-clis-in-one-line-of-code-using-python-321d9aef3be8
https://stribny.name/blog/2020/01/building-command-line-interfaces-in-python/
https://pretagteam.com/question/where-to-patch-calls-for-mocking-inside-a-typerclick-command-python-duplicate
https://testandcode.com/120
https://zetcode.com/python/click/
https://pythonfix.com/pkg/t/typer/
https://click.palletsprojects.com/en/latest/
https://palletsprojects.com/p/click/
https://github.com/pallets/click
https://docs.python.org/3/howto/argparse.html
https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
https://realpython.com/command-line-interfaces-python-argparse/
"""



#@click.command()
#@click.option("-f", "--filename", type=str, default="", help="Filename of markdown file to parse", required=True)
@click.command()
@click.option("-f", "--filename", type=str, default="", help="Filename of markdown file to parse", required=True)
def parse_args(filename):
    click.echo(f"Filename: {filename}")



if __name__=='__main__':
    parse_args()
    if len(sys.argv) > 1:
        inf = sys.argv[1]

        with open(inf, 'r') as f:
            s = f.read()
            print(s)
            jsonData = mdTable2baseJson(s)
            print(jsonData)
            formattedJsonData = json.dumps(jsonData, indent=3)
            print(formattedJsonData)




"""
random, potentially future useful links

https://pyautogui.readthedocs.io/en/latest/quickstart.html
https://code.visualstudio.com/docs/editor/github
https://milvus.io/blog/Implement-Milvus-CLI-by-Python-Click.md
https://slack.dev/bolt-python/concepts
https://github.com/russomi-labs/python-cli-click/wiki/Research

"""
