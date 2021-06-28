"""
CHANGE LOG: Ver :4.2.0
>> 28th June 2021
>> Major Update: Addition of History Clear functionalities
>> Added 3 Buttons in History Frame
    - CLEAR ALL -> deletes all contents of log.txt
    - CLEAR LAST 10 -> deletes last 10 lines of log.txt
    - CLEAR LAST DAY -> deletes records of last date
>> Added message box prompts for confirmations before deleting
>> Added message box showingfo to notify after successful deletion
>> Fixed Frame Glitch:
    - History Frame overlaps Scientific Frame
>> Renamed few variables according to PEP8 Naming Conventions
>> Reduced code by modifying calculate_sc()
COMPATIBLE WITH auxiliary VER: 0.3
"""

import math
from tkinter import BooleanVar, StringVar
from tkinter import Tk, Label, Button, Frame, Entry
from typing import Iterator, Union, Any

from PIL import Image, ImageTk  # type: ignore

from auxiliary import Colours as Col
from auxiliary import make_rad_btn, make_btn, make_sc_btn, make_his_btn
from auxiliary import replace_, modify, save, his_clear


# To Keep window always on top
def aot() -> None:
    if not aot_.get():
        root.attributes("-topmost", True)
        label.configure(fg=Col.aot_color, font="Verdana 12 italic")
        aot_.set(True)

    else:
        root.attributes("-topmost", False)
        label.configure(fg=Col.fg_color, font="Verdana 13")
        aot_.set(False)


# Function Changes theme colors radio button input
def theme(_theme: dict[str, dict] = Col.content["Theme 1"]) -> None:
    # For Theme 2
    if variable_.get() == Col.content["Theme 2"]["Theme Name"]:
        _theme = Col.content["Theme 2"]

    "Normal Frame Colors"
    Col.bg_color = _theme["Background Color"]
    Col.fg_color = _theme["Foreground Color"]
    Col.aot_color = _theme["AOT active Text Color"]
    Col.hover = _theme["Hover Color"]
    Col.radio_color = _theme["Radio Switch Color"]
    Col.radio_fg = _theme["Radio Text Color"]

    "Screen Colors"
    Col.scrn_bg = _theme["Input Screen Color"]["Background Color"]
    Col.scrn_fg = _theme["Input Screen Color"]["Foreground Color"]
    Col.scrn_sb = _theme["Input Screen Color"]["Select Background"]
    Col.scrn_sf = _theme["Input Screen Color"]["Select Foreground"]
    Col.scrn_cur = _theme["Input Screen Color"]["Cursor Color"]

    "Scientific Frame Colors"
    Col.sci_bg = _theme["Scientific Colors"]["Background Color"]
    Col.sci_fg = _theme["Scientific Colors"]["Foreground Color"]
    Col.inv_color = _theme["Scientific Colors"]["|INV| Color"]
    Col.sci_hover = _theme["Scientific Colors"]["Hover Color"]
    Col.sci_hover_inverse = _theme["Scientific Colors"]["Hover Color |INV|"]
    change()


# Function to apply changed colors
def change() -> None:
    label.configure(bg=Col.bg_color, fg=Col.aot_color if aot_.get() else Col.fg_color)
    label0.configure(bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.bg_color)

    [_.configure(bg=Col.bg_color) for _ in (root, main_frame, screen_frame, his_frame, label_frame, sci_frame)]
    screen.configure(bg=Col.scrn_bg, fg=Col.scrn_fg, selectbackground=Col.scrn_sb,
                     selectforeground=Col.scrn_sf, insertbackground=Col.scrn_cur)

    mid_button.configure(bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.bg_color, activeforeground=Col.fg_color)

    for _ in sci_list + sci_list2 + inverted_list:
        _.configure(bg=Col.sci_bg, fg=Col.sci_fg, activebackground=Col.sci_bg, activeforeground=Col.sci_fg)

    inv_color = Col.inv_color if inv_toggle.get() else Col.sci_bg
    inverse_button.configure(bg=inv_color, fg=Col.sci_fg, activebackground=inv_color, activeforeground=Col.sci_fg)

    for _ in radio_list:
        _.configure(bg=Col.bg_color, fg=Col.radio_fg, activebackground=Col.bg_color,
                    activeforeground=Col.fg_color, selectcolor=Col.radio_color)

    for _ in (*widget_list0, *hi_widget_list, all_clear):
        _.configure(bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.fg_color, activeforeground=Col.bg_color)

    for _ in widget_list1 + his_btn_lst:
        _.configure(bg=Col.bg_color, fg=Col.aot_color, activebackground=Col.aot_color, activeforeground=Col.bg_color)


# Function changes color of widgets hovering
def change_on_hovering(event: Any) -> None:
    colour: str = Col.hover
    if event.widget.winfo_parent() in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if event.widget["text"] == "INV":
            colour = Col.sci_hover_inverse if inv_toggle.get() else Col.sci_hover
        else:
            colour = Col.sci_hover
    event.widget["bg"] = colour


# Function returns to normal color when not hovering
def return_on_hovering(event: Any) -> None:
    colour: str = Col.bg_color
    if event.widget.winfo_parent() in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if event.widget["text"] == "INV":
            colour = Col.inv_color if inv_toggle.get() else Col.sci_bg
        else:
            colour = Col.sci_bg
    event.widget["bg"] = colour


# Function to execute Return Key in Screen (Entry Widget)
def enter_click(event: Any) -> None:
    equal_button.flash()
    event.widget = equal_button
    click(event)


# Function to execute click event of  all buttons
def click(event: Any) -> None:
    btn_text: str = event.widget["text"]
    expression: str = replace_(screen.get())
    if btn_text == "=":
        screen.delete(0, "end")
        try:
            answer: str = eval(expression)
            screen.insert(0, answer)
            save(f"\t{expression} = {answer}\n")
        except ZeroDivisionError:
            screen.insert(0, "Can't Divide by Zero")
        except ValueError:
            screen.insert(0, "Value Error")
        except SyntaxError:
            screen.insert(0, "Invalid Input")

    elif btn_text == "⇐":
        screen.delete(len(screen.get()) - 1)
    else:
        screen.insert("end", btn_text)


##################################################################################################################


# Packs Frame to the root window
def history() -> None:
    width, height = 267, 500
    if not his_toggle.get():  # To toggle On
        root.geometry(f"{width * 2 + 6}x{height}+{root.winfo_x() - 132}+{root.winfo_y()}")
        screen_frame.pack_forget()
        sci_frame.pack_forget()
        mid_button.pack_forget()
        mid_frame.pack_forget()
        his_frame.pack(side="right", padx=3)
        show()

        screen_frame.pack()
        if sci_toggle.get():
            sci_frame.pack()
        mid_button.pack()
        mid_frame.pack()
        his_toggle.set(True)

    else:  # To toggle Off
        root.geometry(f'{width}x{height}+{root.winfo_x() + 132}+{root.winfo_y()}')
        his_frame.pack_forget()
        his_toggle.set(False)


# Packing labels to label_frame
def show() -> None:
    global lno, lines
    with open("data/log.txt", "r") as _:
        lines = [line.strip() for line in _.readlines() if not line.startswith("DATE")][::-1]
        lines.append("_________________________________________________________")

    for i in range(line_number, line_number + 5):
        _ = Label(label_frame, bg=Col.bg_color, fg=Col.fg_color, height=0 if i else 3, width=260)
        try:
            _.configure(text=lines[i])
        except IndexError:
            _.configure(text="Not enough data")
        _.configure(font=f"Verdana {10 if abs(i) == 2 else '12 italic' if abs(i) == 1 else '12 bold'}")
        label_list.append(_)
        hi_widget_list.append(_)
        _.bind("<MouseWheel>", scroll)
        _.bind("<Enter>", change_on_hovering)
        _.bind("<Leave>", return_on_hovering)
        _.pack()


# To scroll Down and up
def scroll(event: Any) -> None:
    global lno
    line_number += 1 if event.delta < 0 else -1
    if line_number + 5 > len(lines):
        line_number = -4
    elif line_number < -len(lines):
        line_number = -1

    for _, j in enumerate(range(line_number, line_number + 5)):
        try:
            label_list[_]["text"] = lines[j]
        except IndexError:
            label_list[_]["text"] = "Not enough data"


##################################################################################################################

# Function to toggle Scientific Calculator
def sci_cal() -> None:
    if not sci_toggle.get():  # To Toggle On
        mid_button.pack_forget()
        mid_frame.pack_forget()
        for widget in (*widget_list0, *widget_list1, all_clear):
            widget.configure(height=1, width=4, font="ariel 15")
        sci_frame.pack(padx=5, pady=0)
        mid_button.pack()
        mid_frame.pack()
        sci_toggle.set(True)

    else:  # To Toggle Off
        sci_frame.pack_forget()
        for widget in (*widget_list0, *widget_list1, all_clear):
            widget.configure(height=1, width=2, font="ariel 25 bold")
        sci_toggle.set(False)


# Function(s) to perform Trigonometry
def ln(value): return math.log(float(value))


def sin(value): return math.sin(math.radians(float(value)))


def cos(value): return math.cos(math.radians(float(value)))


def tan(value): return math.tan(math.radians(float(value)))


def log(value): return math.log10(float(value))


def exp(value): return math.exp(float(value))


def asin(value): return math.degrees(math.asin(float(value)))


def acos(value): return math.degrees(math.acos(float(value)))


def atan(value): return math.degrees(math.atan(float(value)))


def fact(value): return math.factorial(int(value))


def sqrt(value): return math.sqrt(float(value))


# Function to insert scientific f(x) in screen
def calculate_sc(event: Any) -> None:
    btn_text = event.widget["text"]
    expression = replace_(screen.get())
    if btn_text in ("(", ")", "^", "!", "10^", "π", "e"):
        screen.insert("end", btn_text)
    elif btn_text == "√x":
        screen.insert("end", "√")
    elif btn_text == "eˣ":
        screen.insert("end", "e^")
    elif btn_text == "DEG":
        screen.delete(0, "end")
        try:
            answer = str(math.degrees(float(expression)))
            screen.insert(0, answer)
        except ValueError:
            screen.insert(0, "Value Error")
    elif btn_text == "RAD":
        screen.delete(0, "end")
        try:
            answer = str(math.radians(float(expression)))
            screen.insert(0, answer)
        except ValueError:
            screen.insert(0, "Value Error")
    else:
        screen.insert("end", f"{btn_text}(")


# Function to toggle Inverse
def inv() -> None:
    if not inv_toggle.get():  # To Toggle On
        sci_upper_frame.pack_forget()
        sci_lower_frame.pack_forget()
        inverse_button.configure(bg=Col.inv_color, fg=Col.sci_fg,
                                 activebackground=Col.inv_color, activeforeground=Col.sci_fg)
        sci_upper_frame2.pack()
        sci_lower_frame.pack()
        inv_toggle.set(True)

    elif inv_toggle.get():  # To Toggle Off
        sci_upper_frame2.pack_forget()
        sci_lower_frame.pack_forget()
        sci_upper_frame.pack()
        sci_lower_frame.pack()
        inv_toggle.set(False)


# The Actual GUI - Front_End
root = Tk()

# Boolean Variables
aot_ = BooleanVar()
modify(root)

# Frames
main_frame = Frame(root)
screen_frame = Frame(root)
mid_frame = Frame(root)
radio_frame = Frame(root)

# Photo Header
photo = ImageTk.PhotoImage(Image.open("icon/icon.png").resize((45, 45), Image.ANTIALIAS))

# Text Header
label = Label(main_frame, text="Calculator", font="Verdana 13 ", justify="center")

# AOT BUTTON
label0 = Button(main_frame, image=photo, justify="center", bd=0, cursor="hand2", command=aot)

# Radio Buttons for selecting theme
variable_ = StringVar(value=Col.theme_name)
# For exclusive radio buttons <Themes>
themes = (Col.content["Theme 1"]["Theme Name"], Col.content["Theme 2"]["Theme Name"])
radio_list = [make_rad_btn(radio_frame, theme_, variable_, theme, 2, col) for col, theme_ in enumerate(themes)]

# Screen Of the calculator - Entry Widget
screen = Entry(screen_frame, relief="sunken", bd=1, justify="right", font="Ariel 30", cursor="arrow")
screen.pack(pady=10, padx=5)

# widget_list0 -> For buttons having usual 'fg_color' foreground
number = iter(range(1, 10))
widget_list0 = [make_btn(mid_frame, next(number), row, col) for row in range(3, 0, -1) for col in range(3)]

# Row Buttons
widget_list0 += [make_btn(mid_frame, bno, 4, col_no) for col_no, bno in enumerate(("00", "0", "."))]

# widget_list1 -> For buttons having exclusive 'aot_color' foreground
widget_list1 = [make_btn(mid_frame, bno, row_no, 3) for row_no, bno in enumerate(("÷", "×", "-", "+"))]

# Few individual Buttons
all_clear = make_btn(mid_frame, "C", 0, 0, lambda: screen.delete(0, "end"))
equal_button = make_btn(mid_frame, "=", 4, 3)
clear_button = make_btn(mid_frame, "⇐", 0, 2)
floor_division = make_btn(mid_frame, "%", 0, 1)

# Inserting into individual lists
widget_list0 += [floor_division, clear_button]
widget_list1.append(equal_button)

# Binding all Buttons to necessary functions
for button in widget_list0 + widget_list1:
    button.bind("<Button-1>", click)
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)

# Binding more Button
screen.bind("<Return>", enter_click)
all_clear.bind("<Enter>", change_on_hovering)
all_clear.bind("<Leave>", return_on_hovering)

# Packing the labels
label.grid(row=0, column=2, columnspan=2)
label0.grid(row=0, column=1, columnspan=1)

# Packing the frames
main_frame.pack(padx=0, pady=0, side="top")
radio_frame.pack(padx=0, pady=0, side="top")
screen_frame.pack(padx=0, pady=0, side="top")

##################################################################################################################

# History Properties
lno = -2

# Boolean Variables
his_toggle = BooleanVar()

# Label List
label_list: list[Label] = list()
lines: list[str] = list()

# History Frames
his_frame = Frame(root, height=420, width=267)
label_frame = Frame(his_frame, height=150, width=260, bd=1, relief="sunken")

# HISTORY
heading = Label(his_frame, text="HISTORY", font="Verdana 15")
label_frame.pack_propagate(False)
his_frame.grid_propagate(False)

# History Button
history_btn = Button(main_frame, command=history, text="H", width=2, height=1, bd=0, font="Verdana 13")
hi_widget_list = [heading, history_btn]

texts = "CLEAR ALL", "CLEAR LAST 10", "CLEAR LAST DAY"
his_btn_lst = [make_his_btn(his_frame, _, row, 0) for row, _ in enumerate(texts, 2)]

for button in his_btn_lst:
    button.bind("<ButtonRelease-1>", his_clear)
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)

his_frame.bind("<MouseWheel>", scroll)
label_frame.bind("<MouseWheel>", scroll)

heading.grid(row=0, column=0)
history_btn.grid(row=0, column=0)
label_frame.grid(row=1, column=0)

##################################################################################################################

# Boolean Variables
sci_toggle = BooleanVar()
inv_toggle = BooleanVar()

# Scientific Frames
sci_frame = Frame(root)
sci_upper_frame = Frame(sci_frame)
sci_upper_frame2 = Frame(sci_frame)
sci_lower_frame = Frame(sci_frame)

mid_button = Button(root, command=sci_cal, text="=", width=22, height=1, bd=0, font="ariel 15", cursor="hand2")

# Advanced Common Scientific Buttons
sci_list = [make_sc_btn(sci_upper_frame, _, 0, col) for col, _ in enumerate(("sin", "cos", "tan", "log", "ln"))]

# Bottom row Buttons
btn_list: Union[Iterator[str], tuple[str, ...]]
btn_list = iter(("(", ")", "^", "√x", "!", "π", "e", " ", "RAD", "DEG"))

sci_list2 = [make_sc_btn(sci_lower_frame, next(btn_list), row, col) for row in range(2) for col in range(5)]

# Special Inverse Buttons
btn_list = "sin⁻¹", "cos⁻¹", "tan⁻¹", "10^", "eˣ"
inverted_list = [make_sc_btn(sci_upper_frame2, text, 0, col_no) for col_no, text in enumerate(btn_list)]

inverse_button = make_sc_btn(sci_lower_frame, "INV", 1, 2, inv)

for button in sci_list + sci_list2 + inverted_list:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", calculate_sc)

inverse_button.bind("<Enter>", change_on_hovering)
inverse_button.bind("<Leave>", return_on_hovering)

mid_button.pack()
mid_frame.pack(padx=10, pady=0)
sci_upper_frame.pack()
sci_lower_frame.pack()

change()
root.mainloop()
##################################################################################################################
