"""
CHANGE LOF: Ver: 1.1
>> 15th July 2021
>> Minor update: Shifting of few functions
>> Added a Class
    - BooleanVar
>> Added 3 functions
    - def change_on_hovering(event: Any) -> None:
    - def return_on_hovering(event: Any) -> None:
    - def aot(root, label) -> None:
COMPATIBLE WITH main VER: 4.2.1
"""

import datetime
import json
import math
from tkinter import Button, Radiobutton, Variable, Frame, Tk
from tkinter.messagebox import askyesno, showinfo
from typing import Union, Callable, Any


class BooleanVar:
    def __init__(self, value=False):
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


class Colours:
    # Parsing Colours
    with open(r"data/themes.json", "r") as f:
        content = json.load(f)

    # Default -> 1st theme
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
        exp: list[str] = list(expression)
        exp.remove(")")
        expression = "".join(exp)

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


# Function to perform history Clear functions
def his_clear(event: Any) -> None:
    btn_txt: str = event.widget["text"]
    if btn_txt == "CLEAR ALL":
        if askyesno(btn_txt, "Are you sure, you want to delete everything?"):
            with open("data/log.txt", "w"):
                showinfo(btn_txt, "Your history is now clean as new")

    elif btn_txt == "CLEAR LAST 10":
        if askyesno(btn_txt, "You are about to delete last 10 records"):
            with open("data/log.txt", "r") as log_:
                lines: list[str] = log_.readlines()
            with open("data/log.txt", "w") as log_:
                log_.writelines(lines[:len(lines) - 10])
            showinfo(btn_txt, "Last 10 Records Cleared ")
    else:
        with open("data/log.txt", "r") as log_:
            lines = log_.readlines()
        if len(lines):  # Will not delete if length < 1
            l_date = [line for line in lines[::-1] if line.startswith("DATE")][0].strip("DATE: ")
            if askyesno(btn_txt, f"You are about to delete records of {l_date}"):
                for line in lines[::-1]:
                    lines.remove(line)
                    if line.startswith("DATE"):
                        break
                with open("data/log.txt", "w") as log_:
                    log_.writelines(lines)
                showinfo(btn_txt, "Records Cleaned successfully")
        else:
            showinfo(btn_txt, "You have no data")


# Function modifies root window
def modify(window: Tk) -> None:
    width, height = 267, 500
    x_cord: int = (window.winfo_screenwidth() - width) // 2
    y_cord: int = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x_cord}+{y_cord}")
    window.wm_iconbitmap("icon/icon.ico")
    window.title("Better Calculator")
    window.resizable(False, False)


def make_btn(parent: Frame, txt: Union[int, str], ro: int, col: int, com=None) -> Button:
    btn: Button = Button(parent, text=txt, width=2, padx=6, font="ariel 25 bold", bd=0, relief="groove", command=com)
    btn.grid(row=ro, column=col)
    return btn


def make_sc_btn(parent: Frame, txt: str, ro: int, col: int, com=None) -> Button:
    btn: Button = Button(parent, text=txt, width=4, font="ariel 15", bd=1, command=com)
    btn.grid(row=ro, column=col)
    return btn


def make_rad_btn(parent: Frame, txt: str, var: Variable, com: Callable, ro: int, col: int) -> Radiobutton:
    btn: Radiobutton = Radiobutton(parent, text=txt, variable=var, value=txt, cursor="hand2", command=com)
    btn.grid(row=ro, column=col)
    return btn


def make_his_btn(parent: Frame, txt: str, ro: int, col: int) -> Button:
    btn: Button = Button(parent, text=txt, width=15, height=1, font="ariel 11", pady=4, bd=0)
    btn.grid(row=ro, column=col)
    return btn


# Function changes color of widgets hovering
def change_on_hovering(event: Any) -> None:
    colour: str = Colours.hover
    if event.widget.winfo_parent() in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if event.widget["text"] == "INV":
            colour = Colours.sci_hover_inverse if inv_toggle.get() else Colours.sci_hover
        else:
            colour = Colours.sci_hover
    event.widget["bg"] = colour


# Function returns to normal color when not hovering
def return_on_hovering(event: Any) -> None:
    colour: str = Colours.bg_color
    if event.widget.winfo_parent() in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if event.widget["text"] == "INV":
            colour = Colours.inv_color if inv_toggle.get() else Colours.sci_bg
        else:
            colour = Colours.sci_bg
    event.widget["bg"] = colour


# To Keep window always on top
def aot(root, label) -> None:
    if aot_.get():
        root.attributes("-topmost", False)
        label.config(fg=Colours.fg_color, font="Verdana 13")
        aot_.set(False)
    else:
        root.attributes("-topmost", True)
        label.config(fg=Colours.aot_color, font="Verdana 12 italic")
        aot_.set(True)


inv_toggle = BooleanVar()
aot_ = BooleanVar()
