#!/usr/bin/env -S python -u
"""
"""

from enum import Enum
import json
import sys

import mistune


class State(Enum):
    INIT = 0
    INFO = 1
    HEADER = 2
    KEYS = 3
    ATTRIBUTES = 4


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inf = sys.argv[1]
        # renderer = JsonRenderer()
        renderer = mistune.renderers.AstRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        with open(inf, 'r') as f:
            s = f.read()
            # print(markdown(s))
            jsonFormattedData = json.dumps(markdown(s), indent=4)
            print(jsonFormattedData)

