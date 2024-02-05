"""
-- MARKDOWN_FORMAT.py
Convinience methods for converting data to a markdown format
"""


def printH1(text: str):
    return f"# {text}"


def printH2(text: str):
    return f"## {text}"


def printBold(text: str):
    return f"**{text}**"


def printItalic(text: str):
    return f"*{text}*"


def printUL(l: list):
    lString = ""

    for item in l:
        lString += f"- {item}\n"

    return lString


def printOL(l: list):
    lString = ""
    for x in range(len(l)):
        lString += f"{x+1}. {l[x]}\n"
    return lString
