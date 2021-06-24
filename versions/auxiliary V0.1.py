"""
CHANGE LOG: Ver :0.1
>> 24th June 2021
>> Major Update:
>> Added 2 functions
    - def createbtn(parent, txt, ro, col) -> Button:
        1. Creates buttons ,grids and returns them
    - def createscibtn(parent, txt, ro, col) -> Button:
        1. Creates scientific buttons, grids them and returns them
>> Added Colours Class to encapsulate colours
>> Added a feature to add '*' before parenthesis
COMPATIBLE WITH main VER: 4.1.1
"""

import datetime
import json
import math
from tkinter import Button


class Colours:
    # Parsing Colours
    with open(r"data/themes.json", "r") as f:
        content = json.load(f)

    # Default -> 1st theme
    # Default Primary Values
    Default = content["Theme 1"]
    theme_name = Default["Theme Name"]

    "Normal Frame Colors"
    bg_color = Default["Background Color"]
    fg_color = Default["Foreground Color"]
    aot_color = Default["AOT active Text Color"]
    hover = Default["Hover Color"]
    radio_color = Default["Radio Switch Color"]
    radio_fg = Default["Radio Text Color"]

    "Screen Colors"
    scrn_bg = Default["Input Screen Color"]["Background Color"]
    scrn_fg = Default["Input Screen Color"]["Foreground Color"]
    scrn_sb = Default["Input Screen Color"]["Select Background"]
    scrn_sf = Default["Input Screen Color"]["Select Foreground"]
    scrn_cur = Default["Input Screen Color"]["Cursor Color"]

    "Scientific Frame Colors"
    sci_bg = Default["Scientific Colors"]["Background Color"]
    sci_fg = Default["Scientific Colors"]["Foreground Color"]
    inv_color = Default["Scientific Colors"]["|INV| Color"]
    sci_hover = Default["Scientific Colors"]["Hover Color"]
    sci_hover_inverse = Default["Scientific Colors"]["Hover Color |INV|"]


# Function:
# 1. Replaces visual elements with real elements
# 2. Adds forgotten parenthesis
# 3. Removes redundant parenthesis
# 4. Adds forgotten 0 before decimal
# 5. Adds forgotten * before parenthesis
def replace_(expression: str) -> str:
    original = ("×", "÷", "^", "π", "e", "sin⁻¹(", "cos⁻¹(", "tan⁻¹(", "!", "√")
    replaced = ("*", "/", "**", str(math.pi), str(math.e), "asin(", "acos(", "atan(", "fact(", "sqrt(")

    # Replacing visual elements with real elements
    for original_, replaced_ in zip(original, replaced):
        expression = expression.replace(original_, replaced_)

    # Adding forgotten parenthesis
    while expression.count("(") > expression.count(")"):
        expression = expression + ")"

    # Removing redundant parenthesis
    while expression.count("(") < expression.count(")"):
        expl = list(expression)
        expl.remove(")")
        expression = "".join(expl)

    # Adding 0 before decimal
    if "." in expression:
        if not expression[expression.find(".") - 1].isnumeric():
            expression = "0.".join(expression.split("."))

    # Adding * before parenthesis
    if "(" in expression:
        if expression[expression.find("(") - 1].isnumeric():
            expression = "*(".join(expression.split("("))

    return expression


# Function to save history
def save(expression):
    today = datetime.date.today()
    isd = f"DATE: {'-'.join(str(today).split('-')[::-1])}\n"
    with open("data/log.txt", "r+") as log_:
        try:
            ldate = [date for date in log_.readlines() if date.startswith("DATE")][-1]
        except IndexError:
            ldate = False
        log_.write(f"{expression}" if ldate == isd else f"{isd}{expression}")


# Function sets geometry and opens root window at the center
def geometry_(window):
    width, height = 267, 500
    x_cord = (window.winfo_screenwidth() - width) // 2
    y_cord = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x_cord}+{y_cord}")


# Function modifies root window
def modify(window):
    geometry_(window)
    window.wm_iconbitmap("icon/icon.ico")
    window.title("Better Calculator")
    window.resizable(height=0, width=0)
    window.configure(bg=Colours.bg_color)


def createbtn(parent, txt, ro, col) -> Button:
    btn = Button(parent, text=txt, width=2, padx=6, font="ariel 25 bold", bd=0, bg=Colours.bg_color,
                 fg=Colours.fg_color if col != 3 else Colours.aot_color,
                 activebackground=Colours.fg_color if col != 3 else Colours.aot_color,
                 activeforeground=Colours.bg_color, relief="groove", border=0)
    btn.grid(row=ro, column=col)
    return btn


def createscibtn(parent, txt, ro, col) -> Button:
    btn = Button(parent, text=txt, width=4, font="ariel 15", bd=1, bg=Colours.sci_bg, fg=Colours.sci_fg,
                 activebackground=Colours.sci_bg, activeforeground=Colours.sci_fg)
    btn.grid(row=ro, column=col)
    return btn
