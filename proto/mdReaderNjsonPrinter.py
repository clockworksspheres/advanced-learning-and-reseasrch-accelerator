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


# class JsonRenderer(mistune.renderers.BaseRenderer):
class JsonRenderer(mistune.renderers.AstRenderer):
    """
    Changing to rendering to inherit the AstRenderer (Abstract Data Type) - which appears to be json
    based anyway..
    """
    def __init__(self):
        super().__init__()
        self.description = []
        self.item_name = None
        self.document = {}
        self.attributes = []
        self.item_attributes = []
        self.cells = []

    def __call__(self):
        if len(self.description) > 0:
            if self.document[self.item_name] is None:
                self.document[self.item_name] = {}
            self.document[self.item_name]["description"] = ''.join(
                self.description)
        if len(self.item_attributes) > 0:
            if self.document[self.item_name] is None:
                self.document[self.item_name] = {}
            self.document[self.item_name]["attributes"] = self.item_attributes
        return json.dumps(self.document)

    def block_code(self, code, language=None):
        return ""

    def block_quote(self, text):
        return ""

    def block_html(self, html):
        return ""

    def header(self, text, level, raw=None):
        self.item_name = text
        self.document = {self.item_name: None}
        return ""

    def hrule(self):
        return ""

    def list(self, body, ordered=True):
        return ""

    def list_item(self, text):
        return ""

    def paragraph(self, text):
        self.description.append(text)
        return ""

    def table(self, header, body):
        keys = self.attributes[0]
        values = self.attributes[1:]
        self.item_attributes = [dict(zip(keys, value)) for value in values]
        return ""

    def table_row(self, content):
        self.attributes.append(list(self.cells))
        self.cells = []
        return ""

    def table_cell(self, content, **flags):
        self.cells.append(content)
        return ""

    def autolink(self, link, is_email=False):
        return ""

    def codespan(self, text):
        return ""

    def double_emphasis(self, text):
        return ""

    def emphasis(self, text):
        return ""

    def image(self, src, title, alt_text):
        return ""

    def linebreak(self):
        return ""

    def newline(self):
        return ""

    def link(self, link, title, content):
        return ""

    def strikethrough(self, text):
        return ""

    def text(self, text):
        return text

    def inline_html(self, text):
        return ""

    def footnote_ref(self, key, index):
        return ""

    def footnote_item(self, key, text):
        return ""

    def footnotes(self, text):
        return ""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inf = sys.argv[1]
        renderer = JsonRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        with open(inf, 'r') as f:
            s = f.read()
            # print(markdown(s))
            jsonFormattedData = json.dumps(markdown(s), indent=4)
            print(jsonFormattedData)

