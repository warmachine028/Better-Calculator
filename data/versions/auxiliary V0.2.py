"""
CHANGE LOG: Ver: 0.2
>> 26th June 2021
>> Major Update: Added 1 function and Type Hinting
>> Added 1 function
    - def make_rad_btn(parent: Frame, txt: str, var: Variable,
                       com: Callable, ro: int, col: int) -> Radiobutton:
        1. Creates radio buttons, grids and returns them
>> Renamed 2 functions:
    - createbtn ->  make_btn
    - createscibtn -> make_sc_btn
    - removed redundant colour settings
>> Removed geometry_() function and merged its functionality in modify()
COMPATIBLE WITH main VER: 4.1.2
"""

import datetime
import json
import math
from tkinter import Button, Radiobutton, Variable, Frame, Tk
from typing import Union, Callable


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
    original: tuple[str, ...] = ("×", "÷", "^", "π", "e", "sin⁻¹(", "cos⁻¹(", "tan⁻¹(", "!", "√")
    replaced: tuple[str, ...] = ("*", "/", "**", str(math.pi), str(math.e), "asin(", "acos(", "atan(", "fact(", "sqrt(")

    # Replacing visual elements with real elements
    for original_, replaced_ in zip(original, replaced):
        expression = expression.replace(original_, replaced_)

    # Adding forgotten parenthesis
    while expression.count("(") > expression.count(")"):
        expression = expression + ")"

    # Removing redundant parenthesis
    while expression.count("(") < expression.count(")"):
        temp: list[str] = list(expression)
        temp.remove(")")
        expression = "".join(temp)

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
def save(expression: str) -> None:
    today: datetime.date = datetime.date.today()
    c_date: str = f"DATE: {'-'.join(str(today).split('-')[::-1])}\n"
    with open("data/log.txt", "r+") as log_:
        try:
            l_date: str = [date for date in log_.readlines() if date.startswith("DATE")][-1]
            log_.write(expression if l_date == c_date else f"{c_date} {expression}")
        except IndexError:
            pass


# Function modifies root window
def modify(window: Tk) -> None:
    width, height = 267, 500
    x_cord: int = (window.winfo_screenwidth() - width) // 2
    y_cord: int = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x_cord}+{y_cord}")
    window.wm_iconbitmap("icon/icon.ico")
    window.title("Better Calculator")
    window.resizable(False, False)


def make_btn(parent: Frame, txt: Union[int, str], ro: int, col: int) -> Button:
    btn: Button = Button(parent, text=txt, width=2, padx=6, font="ariel 25 bold", bd=0, relief="groove", border=0)
    btn.grid(row=ro, column=col)
    return btn


def make_sc_btn(parent: Frame, txt: str, ro: int, col: int) -> Button:
    btn: Button = Button(parent, text=txt, width=4, font="ariel 15", bd=1)
    btn.grid(row=ro, column=col)
    return btn


def make_rad_btn(parent: Frame, txt: str, var: Variable, com: Callable, ro: int, col: int) -> Radiobutton:
    btn: Radiobutton = Radiobutton(parent, text=txt, variable=var, value=txt, cursor="hand2", command=com)
    btn.grid(row=ro, column=col)
    return btn
