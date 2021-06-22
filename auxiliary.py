"""
CHANGE LOG: Ver :0.0
>> 22nd June 2021
>> Major Update: Creation
>> Added 4 functions
    - replace_(expression)
        1. Replaces visual elements with real elements
        2. Adds forgotten parenthesis
        3. Removes redundant parenthesis
        4. Adds forgotten 0 before decimal
    - save(expression) -> To save history of calculations
    - geometry_(window) -> To set geometry and open root window at the center
    - modify(window, bg_colour) -> Function modifies root window
"""

import datetime
import math


# Function:
# 1. Replaces visual elements with real elements
# 2. Adds forgotten parenthesis
# 3. Removes redundant parenthesis
# 4. Adds forgotten 0 before decimal
def replace_(expression):
    original = ("×", "÷", "^", "π", "e", "sin⁻¹(", "cos⁻¹(", "tan⁻¹(", "!", "√")
    replaced = ("*", "/", "**", str(math.pi), str(math.e), "asin(", "acos(", "atan(", "factorial(", "square_root(")

    # Replacing visual elements with real elements
    for original_, replaced_ in zip(original, replaced):
        expression = expression.replace(original_, replaced_)

    # Adding forgotten parenthesis
    while expression.count("(") > expression.count(")"):
        expression = expression + ")"

    # Removing Redundant parenthesis
    while expression.count("(") < expression.count(")"):
        expl = list(expression)
        expl.remove(")")
        expression = "".join(expl)

    # Adding 0 before decimal
    if "." in expression:
        if not expression[expression.find(".") - 1].isnumeric():
            expression = "0.".join(expression.split("."))
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
def modify(window, bg_color):
    geometry_(window)
    window.wm_iconbitmap("icon/icon.ico")
    window.title("Better Calculator")
    window.resizable(height=0, width=0)
    window.configure(bg=bg_color)
