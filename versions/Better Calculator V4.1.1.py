"""
CHANGE LOG: Ver :4.1.1
>> 24th June 2021
>> Minor Update: Reduction & Restructuring of Code
>> Fixed glitch: which let window reopen in centre
   when history button is pressed
>> Shifted colors to class Colours in auxiliary.py
>> Shifted bconfigure() and sc_bconfigure() to auxiliary.py
   as createbtn() and createscibtn()
>> Removed TypeError from click()
>> Reverted lambda functions to normal functions
COMPATIBLE WITH auxiliary VER: 0.1
"""

import math
from tkinter import *

from PIL import Image, ImageTk

import auxiliary as aux
from auxiliary import Colours as Col


# To Keep window always on top
def aot():
    if not aot_.get():  # To Toggle On
        root.attributes("-topmost", True)
        label.configure(fg=Col.aot_color, font="Verdana 12 italic")
        aot_.set(True)

    else:  # To Toggle Off
        root.attributes("-topmost", False)
        label.configure(fg=Col.fg_color, font="Verdana 13")
        aot_.set(False)


# Function Changes theme colors radio button input
def theme():
    _theme = Col.content["Theme 1"]

    # For Theme 2
    if _variable.get() == Col.content["Theme 2"]["Theme Name"]:
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
def change():
    label.configure(bg=Col.bg_color, fg=Col.aot_color if aot_.get() else Col.fg_color)
    label0.configure(bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.bg_color)
    for frame in (root, main_frame, screen_frame, his_frame, label_frame, sci_frame):
        frame.configure(bg=Col.bg_color)

    screen.configure(bg=Col.scrn_bg, fg=Col.scrn_fg, selectbackground=Col.scrn_sb, selectforeground=Col.scrn_sf,
                     insertbackground=Col.scrn_cur)

    mid_button.configure(bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.bg_color, activeforeground=Col.fg_color)

    for widget in sci_list + sci_list2 + inverted_list:
        widget.configure(bg=Col.sci_bg, fg=Col.sci_fg, activebackground=Col.sci_bg, activeforeground=Col.sci_fg)

    if inv_toggle.get():
        inverse_button.configure(bg=Col.inv_color, fg=Col.sci_fg, activebackground=Col.inv_color,
                                 activeforeground=Col.sci_fg)
    else:
        inverse_button.configure(bg=Col.sci_bg, fg=Col.sci_fg, activebackground=Col.sci_bg, activeforeground=Col.sci_fg)

    for radiobutton in radio_list:
        radiobutton.configure(bg=Col.bg_color, fg=Col.radio_fg, activebackground=Col.bg_color,
                              activeforeground=Col.fg_color, selectcolor=Col.radio_color)

    for widget in (*widget_list0, *hi_widget_list, all_clear):
        widget.configure(bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.fg_color, activeforeground=Col.bg_color)

    for widget in widget_list1:
        widget.configure(bg=Col.bg_color, fg=Col.aot_color, activebackground=Col.aot_color,
                         activeforeground=Col.bg_color)


# Function changes color of widgets hovering
def change_on_hovering(event):
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if widget["text"] == "INV":
            widget.configure(bg=Col.sci_hover_inverse if inv_toggle.get() else Col.sci_hover)
        else:
            widget.configure(bg=Col.sci_hover)
    else:
        widget["bg"] = Col.hover


# Function returns to normal color when not hovering
def return_on_hovering(event):
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if widget["text"] == "INV":
            widget.configure(bg=Col.inv_color if inv_toggle.get() else Col.sci_bg)
        else:
            widget.configure(bg=Col.sci_bg)
    else:
        widget["bg"] = Col.bg_color


# Function to execute Return Key in Screen (Entry Widget)
def enter_click(event):
    equal_button.flash()
    event.widget = equal_button
    click(event)


# Function to execute click event of  all buttons
def click(event):
    btn_text = event.widget["text"]
    expression = aux.replace_(screen.get())
    if btn_text == "=":
        screen.delete(0, END)
        try:
            answer = eval(expression)
            screen.insert(0, answer)
            aux.save(f"\t{expression} = {answer}\n")
        except ZeroDivisionError:
            screen.insert(0, "Can't Divide by Zero")
        except ValueError:
            screen.insert(0, "Value Error")
        except SyntaxError:
            screen.insert(0, "Invalid Input")

    elif btn_text == "⇐":
        screen.delete(len(screen.get()) - 1)
    else:
        screen.insert(END, btn_text)


##################################################################################################################


# Packs Frame to the root window
def history():
    width, height = 267, 500
    if not his_toggle.get():  # To toggle On
        root.geometry(f"{width * 2}x{height}+{root.winfo_x() - 132}+{root.winfo_y()}")
        screen_frame.pack_forget()
        sci_frame.pack_forget()
        mid_button.pack_forget()
        Mid_frame.pack_forget()
        his_frame.pack(side=RIGHT, padx=3)
        show()

        screen_frame.pack()
        if sci_toggle.get():
            sci_frame.pack()
        mid_button.pack()
        Mid_frame.pack()
        his_toggle.set(True)

    else:  # To toggle Off
        root.geometry(f'{width}x{height}+{root.winfo_x() + 132}+{root.winfo_y()}')
        his_frame.pack_forget()
        his_toggle.set(False)


# Packing labels to label_frame
def show():
    global lno, lines
    with open("data/log.txt", "r") as _:
        lines = [line.strip() for line in _.readlines() if not line.startswith("DATE")][::-1]
        lines.append("_________________________________________________________")

    for i in range(lno, lno + 5):
        _ = Label(label_frame, bg=Col.bg_color, fg=Col.fg_color, height=0 if i else 3, width=260)
        try:
            _.configure(text=lines[i])
        except IndexError:
            _.configure(text="Not enough data")
        _.configure(font=f"Verdana {'10' if i in (-2, 2) else '12 italic' if i in (-1, 1) else '12 bold'}")
        label_list.append(_)
        hi_widget_list.append(_)
        _.bind("<MouseWheel>", scroll)
        _.bind("<Enter>", change_on_hovering)
        _.bind("<Leave>", return_on_hovering)
        _.pack()


# To scroll Down and up
def scroll(event):
    global lno
    lno += 1 if event.delta < 0 else -1

    if lno + 5 > len(lines):
        lno = -4
    elif lno < -len(lines):
        lno = -1

    for _, j in enumerate(range(lno, lno + 5)):
        try:
            label_list[_].configure(text=lines[j])
        except IndexError:
            label_list[_].configure(text="Not enough data")


##################################################################################################################

# Function to toggle Scientific Calculator
def sci_cal():
    if not sci_toggle.get():  # To Toggle On
        mid_button.pack_forget()
        Mid_frame.pack_forget()
        for widget in (*widget_list0, *widget_list1, all_clear):
            widget.configure(height=1, width=4, font="ariel 15")
        sci_frame.pack(padx=5, pady=0)
        mid_button.pack()
        Mid_frame.pack()
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
def calculate_sc(event):
    btn_text = event.widget["text"]
    expression = aux.replace_(screen.get())
    if btn_text == "sin":
        screen.insert(END, "sin(")
        return
    elif btn_text == "cos":
        screen.insert(END, "cos(")
        return
    elif btn_text == "tan":
        screen.insert(END, "tan(")
        return
    elif btn_text == "log":
        screen.insert(END, "log(")
        return
    elif btn_text == "ln":
        screen.insert(END, "ln(")
        return
    elif btn_text == "√x":
        screen.insert(END, "√")
        return
    elif btn_text == "sin⁻¹":
        screen.insert(END, "sin⁻¹(")
        return
    elif btn_text == "cos⁻¹":
        screen.insert(END, "cos⁻¹(")
        return
    elif btn_text == "tan⁻¹":
        screen.insert(END, "tan⁻¹(")
        return
    elif btn_text == "eˣ":
        screen.insert(END, "e^")
        return
    elif btn_text == "DEG":
        try:
            answer = str(math.degrees(float(expression)))
        except ValueError:
            screen.delete(0, END)
            screen.insert(0, "Value Error")
            return
    elif btn_text == "RAD":
        try:
            answer = str(math.radians(float(expression)))
        except ValueError:
            screen.delete(0, END)
            screen.insert(0, "Value Error")
            return
    else:
        screen.insert(END, btn_text)
        return
    screen.delete(0, END)
    screen.insert(0, answer)


# Function to toggle Inverse
def inv():
    if not inv_toggle.get():  # To Toggle On
        sci_upper_frame.pack_forget()
        sci_lower_frame.pack_forget()
        inverse_button.configure(bg=Col.inv_color, fg=Col.sci_fg, activebackground=Col.inv_color,
                                 activeforeground=Col.sci_fg)
        sci_upper_frame2.pack()
        sci_lower_frame.pack()
        inv_toggle.set(True)

    elif inv_toggle.get():  # To Toggle Off
        sci_upper_frame2.pack_forget()
        sci_lower_frame.pack_forget()
        sci_upper_frame.pack()
        sci_lower_frame.pack()
        inv_toggle.set(False)


# Button lists
widget_list0 = list()  # For buttons having usual 'fg_color' foreground
widget_list1 = list()  # For buttons having exclusive 'aot_color' foreground
radio_list = list()  # For exclusive radio buttons <Themes>

# The Actual GUI - Front_End
root = Tk()

# Boolean Variables
aot_ = BooleanVar(value=False)
aux.modify(root)

# Frames
main_frame = Frame(root, bd=0, bg=Col.bg_color)
screen_frame = Frame(root, bd=0, bg=Col.bg_color)
Mid_frame = Frame(root, bd=0, bg=Col.bg_color)
radio_frame = Frame(root, bd=0, bg=Col.bg_color)

# Photo Header
photo = ImageTk.PhotoImage(Image.open("icon/icon.png").resize((45, 45), Image.ANTIALIAS))

# Text Header
label = Label(main_frame, text="Calculator", font="Verdana 13 ", fg=Col.fg_color, bg=Col.bg_color, justify=CENTER)

# AOT BUTTON
label0 = Button(main_frame, image=photo, bg=Col.bg_color, activebackground=Col.bg_color, justify=CENTER, bd=0,
                cursor="hand2", command=aot)

# Radio Buttons for selecting theme
_variable = StringVar(value=Col.theme_name)

for column_number, theme_ in enumerate((Col.content["Theme 1"]["Theme Name"], Col.content["Theme 2"]["Theme Name"])):
    _ = Radiobutton(radio_frame, command=theme, text=theme_, variable=_variable, value=theme_,
                    selectcolor=Col.radio_color, bg=Col.bg_color, fg=Col.radio_fg, cursor="hand2",
                    activebackground=Col.bg_color, activeforeground=Col.fg_color)
    _.grid(row=2, column=column_number + 1)
    radio_list.append(_)

# Screen Of the calculator - Entry Widget
screen = Entry(screen_frame, relief=SUNKEN, bg=Col.scrn_bg, fg=Col.scrn_fg, selectbackground=Col.scrn_sb,
               selectforeground=Col.scrn_sf, borderwidth=1, justify=RIGHT, font="Ariel 30", cursor="arrow",
               insertbackground=Col.scrn_cur)

screen.pack(side=TOP, pady=10, padx=10)

# Number Buttons
bno = 1
for row_number in range(3, 0, -1):
    for col_no in range(3):
        widget_list0.append(aux.createbtn(Mid_frame, bno, row_number, col_no))
        bno += 1

# Row Buttons
for col_no, bno in enumerate(("00", "0", ".")):
    widget_list0.append(aux.createbtn(Mid_frame, bno, 4, col_no))

# Column Buttons
for row_number, bno in enumerate(("÷", "×", "-", "+")):
    widget_list1.append(aux.createbtn(Mid_frame, bno, row_number, 3))

# Few individual Buttons
equal_button = aux.createbtn(Mid_frame, "=", 4, 3)
clear_button = aux.createbtn(Mid_frame, "⇐", 0, 2)
floor_division = aux.createbtn(Mid_frame, "%", 0, 1)
all_clear = aux.createbtn(Mid_frame, "C", 0, 0)
all_clear.configure(command=lambda: screen.delete(0, END))

# Inserting into individual lists
widget_list0.append(floor_division)
widget_list0.append(clear_button)
widget_list1.append(equal_button)

# Binding all Buttons to necessary functions
for button in widget_list0 + widget_list1:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", click)

# Binding more Button
screen.bind("<Return>", enter_click)
all_clear.bind("<Enter>", change_on_hovering)
all_clear.bind("<Leave>", return_on_hovering)

# Packing the labels
label0.grid(row=0, column=1, columnspan=1)
label.grid(row=0, column=2, columnspan=2)

# Packing the frames
main_frame.pack(padx=0, pady=0, side=TOP)
radio_frame.pack(padx=0, pady=0, side=TOP)
screen_frame.pack(padx=0, pady=0, side=TOP)

##################################################################################################################

# History Properties
lno = -2

# Boolean Variables
his_toggle = BooleanVar(value=False)

# Label List
label_list = list()
lines = list()

# History Frames
his_frame = Frame(root, bg=Col.bg_color, height=420, width=267)
label_frame = Frame(his_frame, bg=Col.bg_color, height=150, width=260, bd=1, relief=SUNKEN)

# HISTORY
heading = Label(his_frame, text="HISTORY", font="Verdana 15", bg=Col.bg_color, fg=Col.fg_color, justify=CENTER)
label_frame.pack_propagate(False)
his_frame.grid_propagate(False)

# History Button
history_btn = Button(main_frame, command=history, text="H", width=2, height=1, font="Verdana 13", bd=0, bg=Col.bg_color,
                     fg=Col.fg_color, activebackground=Col.fg_color, activeforeground=Col.bg_color, relief="groove",
                     border=0)
hi_widget_list = [heading, history_btn]

label_frame.bind("<MouseWheel>", scroll)
his_frame.bind("<MouseWheel>", scroll)

history_btn.grid(row=0, column=0)
heading.grid(row=0, column=0)
label_frame.grid(row=1, column=0)

##################################################################################################################

# Boolean Variables
sci_toggle = BooleanVar(value=False)
inv_toggle = BooleanVar(value=False)

# Button lists
sci_list = list()
sci_list2 = list()
inverted_list = list()

# Scientific Frames
sci_frame = Frame(root, bg=Col.sci_bg)
sci_upper_frame = Frame(sci_frame, bg=Col.sci_bg)
sci_upper_frame2 = Frame(sci_frame, bg=Col.sci_bg)
sci_lower_frame = Frame(sci_frame, bg=Col.sci_bg)
sci_upper_frame.pack()
sci_lower_frame.pack()
mid_button = Button(root, command=sci_cal, text="=", width=22, height=1, font="ariel 15", bd=0, cursor="hand2",
                    bg=Col.bg_color, fg=Col.fg_color, activebackground=Col.bg_color, activeforeground=Col.fg_color)

# Advanced Common Scientific Buttons
for col_no, text in enumerate(("sin", "cos", "tan", "log", "ln")):
    sci_list.append(aux.createscibtn(sci_upper_frame, text, 0, col_no))

# Bottom row Buttons
btn_list = iter(("(", ")", "^", "√x", "!", "π", "e", " ", "RAD", "DEG"))
for row_no in range(2):
    for col_no in range(5):
        sci_list2.append(aux.createscibtn(sci_lower_frame, next(btn_list), row_no, col_no))

# Special Inverse Buttons
for col_no, text in enumerate(("sin⁻¹", "cos⁻¹", "tan⁻¹", "10^", "eˣ")):
    inverted_list.append(aux.createscibtn(sci_upper_frame2, text, 0, col_no))

inverse_button = aux.createscibtn(sci_lower_frame, "INV", 1, 2)
inverse_button.configure(command=inv)

for button in sci_list + sci_list2 + inverted_list:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", calculate_sc)

inverse_button.bind("<Enter>", change_on_hovering)
inverse_button.bind("<Leave>", return_on_hovering)

mid_button.pack()
Mid_frame.pack(padx=10, pady=0)

root.mainloop()
##################################################################################################################
