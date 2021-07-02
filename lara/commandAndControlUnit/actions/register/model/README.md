# Model

Class or object defining data models used by this pattern.

Classes should minimally contain getters and setters for each of the data components, and a custom exception for attempting to access non-existent contents.

Initial data structure intended is a dictionary with the structure defined by one of the following:

* markdown table files of Title = Link pairs
* RIS data files
* bib files (latex?)
* Zotero data structure

future plans include data structures defined by 

* Mendelay
* Endnote

however, it may be more prudent to house and manipulate the data in a modified RIS format and use the transformer to load and save data to each of Zotero, Mendelay and Endnote.

