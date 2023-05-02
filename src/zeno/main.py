from thunno2.lexer import tokenise
from thunno2.flags import run
from thunno2.version import THUNNO_VERSION
import getkey
import os

""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"


def colourise(code):
    ret = ""
    for chars, desc, other in code:
        if "number" in desc:
            ret += CYAN + chars
        elif (
            "string" in desc
            or "dictionary" in desc
            or "character" in desc
            or "alphabetic" in desc
        ):
            ret += BROWN + chars
        elif "list" in desc:
            ret += RED + chars
        elif "print" in desc:
            ret += DARK_GRAY + chars
        elif desc == "digraph":
            ret += GREEN + chars
        elif desc == "constant":
            ret += LIGHT_PURPLE + chars
        elif "single function" in desc or desc == "outer product":
            ret += LIGHT_BLUE + chars
        elif desc in ("context variable", "iteration index"):
            ret += LIGHT_RED + chars
        elif desc == "while loop":
            ret += LIGHT_BLUE + chars
            cond, body = other
            ret += colourise(cond)
            ret += LIGHT_BLUE + ";"
            ret += colourise(body)
            ret += LIGHT_BLUE + ")"
        elif isinstance(other, list):
            ret += LIGHT_BLUE + chars
            ret += colourise(other)
            ret += LIGHT_BLUE + ("}" if chars == "{" else ";")
        else:
            ret += END + chars
    return ret


def remove_colours(code):
    return "".join(c for c in code if len(repr(c)) < 5)


def get_colours(code):
    tokenised = tokenise(code)[1]
    colourised = colourise(tokenised)
    # The lexer autocompletes uncompleted string literals
    if len(remove_colours(colourised)) > len(code):
        while code[-1] != colourised[-1]:
            colourised = colourised[:-1]
    return colourised


def main():
    os.system("clear")
    print(END + "Thunno", THUNNO_VERSION, "interpreter")
    print("Press CTRL + H for help\n")
    print("Code:")
    things = {"code": "", "inputs": "", "flags": "", "help": ""}
    curr = "code"
    while True:
        key = getkey.getkey()
        if key == "\x7f":  # Backspace
            things[curr] = things[curr][:-1]
        elif key == "\x12":  # CTRL + R
            os.system("clear")
            print(END + "Flags:", things["flags"])
            print("\nCode:", get_colours(things["code"]))
            print(END + "\nInputs", things["inputs"])
            print("\nOutput:")
            run(things["flags"], tokenise(things["code"])[1], things["inputs"])
            break
        elif key == "\x04":  # CTRL + D
            curr = "code"
        elif key == "\x06":  # CTRL + F
            curr = "flags"
        elif key == "\x07":  # CTRL + G
            curr = "inputs"
        elif key == "\x08":  # CTRL + H
            os.system("clear")
            print(END + "Thunno", THUNNO_VERSION, "interpreter\n")
            print("CTRL + D \t Switch to code")
            print("CTRL + F \t Switch to flags")
            print("CTRL + G \t Switch to inputs")
            print("CTRL + R \t Run code")
            print("\nPress CTRL + H to exit this help message")
            while getkey.getkey() != "\x08":
                pass
        else:
            things[curr] += key
        os.system("clear")
        print(END + "Thunno", THUNNO_VERSION, "interpreter")
        print("Press CTRL + H for help\n")
        print(curr.title() + ":")
        if curr == "code":
            print(get_colours(things["code"]))
        else:
            print(things[curr])
