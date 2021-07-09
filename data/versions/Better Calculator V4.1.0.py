"""
CHANGE LOG: Ver :4.1.0
>> 22nd June 2021
>> Minor Update: Reduction & Restructuring of Code
>> Created new helper file 'auxiliary.py'
>> Shifted 4 Functions into helper file: (see changelog: Auxiliary.py)
>> Restructured functions in main.py
    - imports
    - functions
    - body
>> Added 2 new functions:
    - bconfigure(button, text, ro, col) -> Configures Button properties & packs
    - sc_bconfigure(button, text, ro, col) -> Configures Scientific Button properties & packs
>> Replaced all toggle variables to BooleanVars
   for easy function access (no globals)
>> Replaced Trigonometry functions to lambda functions
>> COMPATIBLE WITH auxiliary VER: 0.0
"""

import json
import math
from tkinter import *

from PIL import Image, ImageTk

import auxiliary as aux


# To Keep window always on top
def aot():
    if not aot_.get():  # To Toggle On
        root.attributes("-topmost", True)
        label.configure(fg=aot_color, font="Verdana 12 italic")
        aot_.set(True)

    else:  # To Toggle Off
        root.attributes("-topmost", False)
        label.configure(fg=fg_color, font="Verdana 13")
        aot_.set(False)


# Function Changes theme colors radio button input
def theme():
    global bg_color, fg_color, aot_color, hover, radio_color
    global scrn_bg, scrn_fg, scrn_sb, scrn_sf, scrn_cur
    global sci_bg, sci_fg, inv_color, sci_hover, radio_fg, sci_hover_inverse

    _theme = content["Theme 1"]

    # For Theme 2
    if _variable.get() == content["Theme 2"]["Theme Name"]:
        _theme = content["Theme 2"]

    "Normal Frame Colors"
    bg_color = _theme["Background Color"]
    fg_color = _theme["Foreground Color"]
    aot_color = _theme["AOT active Text Color"]
    hover = _theme["Hover Color"]
    radio_color = _theme["Radio Switch Color"]
    radio_fg = _theme["Radio Text Color"]

    "Screen Colors"
    scrn_bg = _theme["Input Screen Color"]["Background Color"]
    scrn_fg = _theme["Input Screen Color"]["Foreground Color"]
    scrn_sb = _theme["Input Screen Color"]["Select Background"]
    scrn_sf = _theme["Input Screen Color"]["Select Foreground"]
    scrn_cur = _theme["Input Screen Color"]["Cursor Color"]

    "Scientific Frame Colors"
    sci_bg = _theme["Scientific Colors"]["Background Color"]
    sci_fg = _theme["Scientific Colors"]["Foreground Color"]
    inv_color = _theme["Scientific Colors"]["|INV| Color"]
    sci_hover = _theme["Scientific Colors"]["Hover Color"]
    sci_hover_inverse = _theme["Scientific Colors"]["Hover Color |INV|"]
    change()


# Function to apply changed colors
def change():
    label.configure(bg=bg_color, fg=aot_color if aot_.get() else fg_color)
    label0.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)
    for frame in (root, main_frame, screen_frame, his_frame, label_frame, sci_frame):
        frame.configure(bg=bg_color)

    screen.configure(bg=scrn_bg, fg=scrn_fg, selectbackground=scrn_sb, selectforeground=scrn_sf,
                     insertbackground=scrn_cur)

    mid_button.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, activeforeground=fg_color)

    for widget in sci_list + sci_list2 + inverted_list:
        widget.configure(bg=sci_bg, fg=sci_fg, activebackground=sci_bg, activeforeground=sci_fg)

    if inv_toggle.get():
        inverse_button.configure(bg=inv_color, fg=sci_fg, activebackground=inv_color, activeforeground=sci_fg)
    else:
        inverse_button.configure(bg=sci_bg, fg=sci_fg, activebackground=sci_bg, activeforeground=sci_fg)

    for radiobutton in radio_list:
        radiobutton.configure(bg=bg_color, fg=radio_fg, activebackground=bg_color, activeforeground=fg_color,
                              selectcolor=radio_color)

    for widget in (*widget_list0, *hi_widget_list, all_clear):
        widget.configure(bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color)

    for widget in widget_list1:
        widget.configure(bg=bg_color, fg=aot_color, activebackground=aot_color, activeforeground=bg_color)


# Configures Button properties and packs them
def bconfigure(btn, txt, ro, col):
    btn.configure(text=txt, width=2, padx=6, font="ariel 25 bold", bd=0, bg=bg_color, fg=fg_color,
                  activebackground=fg_color, activeforeground=bg_color, relief="groove", border=0)
    btn.grid(row=ro, column=col)


# Function changes color of widgets hovering
def change_on_hovering(event):
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if widget["text"] == "INV":
            widget.configure(bg=sci_hover_inverse if inv_toggle.get() else sci_hover)
        else:
            widget.configure(bg=sci_hover)
    else:
        widget["bg"] = hover


# Function returns to normal color when not hovering
def return_on_hovering(event):
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in (".!frame6.!frame", ".!frame6.!frame2", ".!frame6.!frame3"):
        if widget["text"] == "INV":
            widget.configure(bg=inv_color if inv_toggle.get() else sci_bg)
        else:
            widget.configure(bg=sci_bg)
    else:
        widget["bg"] = bg_color


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
        except TypeError:
            screen.insert(0, "No Input")

    elif btn_text == "⇐":
        expression = screen.get()
        expression = expression[0: len(expression) - 1]
        screen.delete(0, END)
        screen.insert(0, expression)
    else:
        screen.insert(END, btn_text)


##################################################################################################################

# Packs Frame to the root window
def history():
    width, height = root.winfo_width() * 2, root.winfo_height()
    x_cord = (root.winfo_screenwidth() - width) // 2
    y_cord = (root.winfo_screenheight() - height) // 2

    if not his_toggle.get():  # To toggle On
        root.geometry(f"{width}x{height}+{x_cord}+{y_cord}")
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
        aux.geometry_(root)
        his_frame.pack_forget()
        his_toggle.set(False)


# Packing labels to label_frame
def show():
    global lno, lines
    with open("data/log.txt", "r") as _:
        lines = [line.strip() for line in _.readlines() if not line.startswith("DATE")][::-1]
        lines.append("_________________________________________________________")

    for i in range(lno, lno + 5):
        _ = Label(label_frame, bg=bg_color, fg=fg_color, height=0 if i else 3, width=260)
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
ln = lambda value: math.log(float(value))
sin = lambda value: math.sin(math.radians(float(value)))
cos = lambda value: math.cos(math.radians(float(value)))
tan = lambda value: math.tan(math.radians(float(value)))
log = lambda value: math.log10(float(value))
exp = lambda value: math.exp(float(value))
asin = lambda value: math.degrees(math.asin(float(value)))
acos = lambda value: math.degrees(math.acos(float(value)))
atan = lambda value: math.degrees(math.atan(float(value)))
factorial = lambda value: math.factorial(int(value))
square_root = lambda value: math.sqrt(float(value))


def sc_bconfigure(btn, txt, row, col):
    btn.configure(text=txt, width=4, font="ariel 15", bd=1, bg=sci_bg, fg=sci_fg, activebackground=sci_bg,
                  activeforeground=sci_fg)
    btn.grid(row=row, column=col)


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
        inverse_button.configure(bg=inv_color, fg=sci_fg, activebackground=inv_color, activeforeground=sci_fg)
        sci_upper_frame2.pack()
        sci_lower_frame.pack()
        inv_toggle.set(True)


    elif inv_toggle.get():  # To Toggle Off
        sci_upper_frame2.pack_forget()
        sci_lower_frame.pack_forget()
        sci_upper_frame.pack()
        sci_lower_frame.pack()
        inv_toggle.set(False)


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

# Button lists
widget_list0 = list()  # For buttons having usual 'fg_color' foreground
widget_list1 = list()  # For buttons having exclusive 'aot_color' foreground
radio_list = list()  # For exclusive radio buttons <Themes>

# The Actual GUI - Front_End
root = Tk()

# Boolean Variables
aot_ = BooleanVar(value=False)
aux.modify(root, bg_color)

# Frames
main_frame = Frame(root, bd=0, bg=bg_color)
screen_frame = Frame(root, bd=0, bg=bg_color)
Mid_frame = Frame(root, bd=0, bg=bg_color)
radio_frame = Frame(root, bd=0, bg=bg_color)

# Photo Header
image = Image.open("icon/icon.png")
photo = ImageTk.PhotoImage(image.resize((45, 45), Image.ANTIALIAS))

# Text Header
label = Label(main_frame, text="Calculator", font="Verdana 13 ", fg=fg_color, bg=bg_color, justify=CENTER)

# AOT BUTTON
label0 = Button(main_frame, image=photo, bg=bg_color, activebackground=bg_color, justify=CENTER, bd=0, cursor="hand2",
                command=aot)

# Radio Buttons for selecting theme
_variable = StringVar(value=theme_name)

for column_number, theme_ in enumerate((content["Theme 1"]["Theme Name"], content["Theme 2"]["Theme Name"])):
    _ = Radiobutton(radio_frame, command=theme, text=theme_, variable=_variable, value=theme_, selectcolor=radio_color,
                    bg=bg_color, fg=radio_fg, cursor="hand2", activebackground=bg_color, activeforeground=fg_color)
    _.grid(row=2, column=column_number + 1)
    radio_list.append(_)

# Screen Of the calculator - Entry Widget
screen = Entry(screen_frame, relief=SUNKEN, bg=scrn_bg, fg=scrn_fg, selectbackground=scrn_sb, selectforeground=scrn_sf,
               borderwidth=1, justify=RIGHT, font="Ariel 30", cursor="arrow", insertbackground=scrn_cur)

screen.pack(side=TOP, pady=10, padx=10)

# Number Buttons
button_text = 1
for row_number in range(3, 0, -1):
    for column_number in range(3):
        _ = Button(Mid_frame)
        bconfigure(_, button_text, row_number, column_number)
        button_text += 1
        widget_list0.append(_)

# Row Buttons
for column_number, button_text in enumerate(("00", "0", ".")):
    _ = Button(Mid_frame)
    bconfigure(_, button_text, 4, column_number)
    widget_list0.append(_)

# Column Buttons
for row_number, button_text in enumerate(("÷", "×", "-", "+")):
    _ = Button(Mid_frame)
    bconfigure(_, button_text, row_number, 3)
    widget_list1.append(_)

# Few individual Buttons
equal_button = Button(Mid_frame)
bconfigure(equal_button, "=", 4, 3)

clear_button = Button(Mid_frame)
bconfigure(clear_button, "⇐", 0, 2)

all_clear = Button(Mid_frame, command=lambda: screen.delete(0, END))
bconfigure(all_clear, "C", 0, 0)

floor_division = Button(Mid_frame)
bconfigure(floor_division, "%", 0, 1)

# Inserting into individual lists
widget_list0.append(floor_division)
widget_list0.append(clear_button)
widget_list1.append(equal_button)

# Binding all Buttons to necessary functions
for button in widget_list0 + widget_list1:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", click)

all_clear.bind("<Enter>", change_on_hovering)
all_clear.bind("<Leave>", return_on_hovering)

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
his_frame = Frame(root, bg=bg_color, height=420, width=267)
label_frame = Frame(his_frame, bg=bg_color, height=150, width=260, bd=1, relief=SUNKEN)

# HISTORY
heading = Label(his_frame, text="HISTORY", font="Verdana 15", bg=bg_color, fg=fg_color, justify=CENTER)
label_frame.pack_propagate(False)
his_frame.grid_propagate(False)

# History Button
history_btn = Button(main_frame, command=history, text="H", width=2, height=1, font="Verdana 13", bd=0, bg=bg_color,
                     fg=fg_color, activebackground=fg_color, activeforeground=bg_color, relief="groove", border=0)
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
sci_frame = Frame(root, bg=sci_bg)
sci_upper_frame = Frame(sci_frame, bg=sci_bg)
sci_upper_frame2 = Frame(sci_frame, bg=sci_bg)
sci_lower_frame = Frame(sci_frame, bg=sci_bg)
sci_upper_frame.pack()
sci_lower_frame.pack()
mid_button = Button(root, command=sci_cal, text="=", width=22, height=1, font="ariel 15", bd=0, cursor="hand2",
                    bg=bg_color, fg=fg_color, activebackground=bg_color, activeforeground=fg_color)

# Advanced Common Scientific Buttons
for column_number, text in enumerate(("sin", "cos", "tan", "log", "ln")):
    _ = Button(sci_upper_frame)
    sc_bconfigure(_, text, 0, column_number)
    sci_list.append(_)

# Bottom row Buttons
bno = 0
button_list2 = ["(", ")", "^", "√x", "!", "π", "e", " ", "RAD", "DEG"]
for row_number in range(2):
    for column_number in range(5):
        _ = Button(sci_lower_frame)
        sc_bconfigure(_, button_list2[bno], row_number, column_number)
        sci_list2.append(_)
        bno += 1

# Special Inverse Buttons
button_list_inverted = ["sin⁻¹", "cos⁻¹", "tan⁻¹", "10^", "eˣ"]
for column_number, text in enumerate(button_list_inverted):
    _ = Button(sci_upper_frame2)
    sc_bconfigure(_, text, 0, column_number)
    inverted_list.append(_)

# Individual Buttons
inverse_button = Button(sci_lower_frame, command=inv)
sc_bconfigure(inverse_button, "INV", 1, 2)

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
