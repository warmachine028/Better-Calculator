"""
CHANGE LOG: Ver : 3.3
>> 2nd January 2021
>> Fixed redundant outputs on console
>> Fixed |INV| button activebackground  
   colour when |INV| activated

"""

import json
import math
from tkinter import *
from PIL import Image, ImageTk

# Parsing Colours
with open(r"data/themes.json", "r") as f:
    content = json.load(f)

Default = content["Theme 1"]
theme_name = Default["Theme Name"]
# Default Primary Values

"Normal Frame Colors"
bg_color = Default["Background Color"]
fg_color = Default["Foreground Color"]
aot_color = Default["AOT active Text Color"]
hover = Default["Hover Color"]
radio_color = Default["Radio Switch Color"]

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

# Common Properties
b_font = "ariel 25 bold"
b_relief = "groove"
b_border = 0
b_width = 2
b_border_width = 0

# Boolean Variables
aot_toggle = False

# Button lists
widget_list0 = list()  # For buttons having usual 'fg_color' foreground
widget_list1 = list()  # For buttons having exclusive 'aot_color' foreground
radio_list = list()  # For exclusive radio buttons <Themes>


# some Functions - Front_end
# To Keep window always on top
def aot():
    """To Keep window always on top"""
    global aot_toggle

    # To Toggle On
    if not aot_toggle:
        root.attributes("-topmost", True)
        label.configure(fg=aot_color, font="Verdana 12 italic")
        aot_toggle = True

    # To Toggle Off
    else:
        root.attributes("-topmost", False)
        label.configure(fg=fg_color, font="Verdana 13")
        aot_toggle = False


# Function Changes theme colors radio button input
def theme():
    global bg_color, fg_color, aot_color, hover, radio_color
    global scrn_bg, scrn_fg, scrn_sb, scrn_sf, scrn_cur
    global sci_bg, sci_fg, inv_color, sci_hover, sci_hover_inverse

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


# Function to set the changed colors to the application
def change():
    root.configure(bg=bg_color)
    label0.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)

    if aot_toggle:
        label.configure(bg=bg_color, fg=aot_color)
    else:
        label.configure(bg=bg_color, fg=fg_color)

    sci_upper_frame.configure(bg=sci_bg)
    main_frame.configure(bg=bg_color)
    screen_frame.configure(bg=bg_color)

    screen.configure(
        bg=scrn_bg, fg=scrn_fg,
        selectbackground=scrn_sb,
        selectforeground=scrn_fg,
        insertbackground=scrn_cur)

    mid_button.configure(
        bg=bg_color, fg=fg_color,
        activebackground=bg_color,
        activeforeground=fg_color)

    for widget in sci_list + sci_list2 + inverted_list:
        widget.configure(
            bg=sci_bg, fg=sci_fg,
            activebackground=sci_bg,
            activeforeground=sci_fg)

    if inv_toggle:
        inverse_button.configure(
            bg=inv_color, fg=sci_fg,
            activebackground=inv_color,
            activeforeground=sci_fg)
    else:
        inverse_button.configure(
            bg=sci_bg, fg=sci_fg,
            activebackground=sci_bg,
            activeforeground=sci_fg)

    for radiobutton in radio_list:
        radiobutton.configure(
            bg=bg_color, fg=fg_color,
            activebackground=bg_color,
            activeforeground=fg_color,
            selectcolor=radio_color)

    for widget in widget_list0:
        widget.configure(
            bg=bg_color, fg=fg_color,
            activebackground=fg_color,
            activeforeground=bg_color)

    for widget in widget_list1:
        widget.configure(
            bg=bg_color, fg=aot_color,
            activebackground=aot_color,
            activeforeground=bg_color)

    all_clear.configure(
        bg=bg_color, fg=fg_color,
        activebackground=fg_color,
        activeforeground=bg_color)


# Function changes color of widgets hovering
def change_on_hovering(event):
    """Function changes color of widgets hovering"""
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in [".!frame4.!frame", ".!frame4.!frame2", ".!frame4.!frame3"]:
        if widget["text"] == "INV":
            widget.configure(
                bg=sci_hover_inverse) if inv_toggle else widget.configure(
                bg=sci_hover)
            return
        else:
            widget.configure(bg=sci_hover)
        return
    widget["bg"] = hover


# Function returns to normal color when not hovering
def return_on_hovering(event):
    """Function returns to original color when not hovering"""
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in [".!frame4.!frame", ".!frame4.!frame2", ".!frame4.!frame3"]:
        if widget["text"] == "INV":
            widget.configure(bg=inv_color) if inv_toggle else widget.configure(
                bg=sci_bg
            )
            return
        else:
            widget.configure(bg=sci_bg)
        return
    widget["bg"] = bg_color


# some Functions - Back_end
# Function to execute Return Key in Screen (Entry Widget)
def enter_click(event):
    """Function to execute Return Key in Screen (Entry Widget)"""
    event.widget = equal_button
    click(event)


# Function to execute click event of  all buttons
def click(event):
    btn_text = event.widget["text"]
    expression = replace_(screen.get())
    if btn_text == "=":
        try:
            answer = eval(expression)
            screen.delete(0, END)
            screen.insert(0, answer)
        except ZeroDivisionError:
            screen.delete(0, END)
            screen.insert(0, "Can't Divide by Zero")
        except ValueError:
            screen.delete(0, END)
            screen.insert(0, "Value Error")
        except SyntaxError:
            screen.delete(0, END)
            screen.insert(0, "Invalid Input")
        except TypeError:
            screen.delete(0, END)
            screen.insert(0, "No Input")
        return

    elif btn_text == "⇐":
        expression = screen.get()
        expression = expression[0: len(expression) - 1]
        screen.delete(0, END)
        screen.insert(0, expression)
        return

    else:
        screen.insert(END, btn_text)


# Function Replaces visual elements with functioning elements adds and removes redundant parenthesis
def replace_(expression):
    """Function Replaces visual elements with functioning elements ,adds and removes redundant parenthesis."""
    original = ["×", "÷", "^", "π", "e", "sin⁻¹(", "cos⁻¹(", "tan⁻¹(", "!", "√"]
    replaced = [
        "*",
        "/",
        "**",
        str(math.pi),
        str(math.e),
        "asin(",
        "acos(",
        "atan(",
        "factorial(",
        "square_root(",
    ]

    for original_, replaced_ in zip(original, replaced):
        new_text = expression.replace(original_, replaced_)
        expression = new_text

    # Adding required parenthesis
    if expression.count("(") > expression.count(")"):
        expression = expression + ")"

    # Removing Redundant parenthesis
    while expression.count("(") < expression.count(")"):
        expl = list(expression)
        expl.remove(")")
        expression = "".join(expl)
    return expression


# The Actual GUI - Front_End
root = Tk()

root.geometry("267x500")
root.wm_iconbitmap("icon/icon.ico")
root.title("Better Calculator")
root.resizable(height=0, width=0)
root.configure(bg=bg_color)
# Frames
main_frame = Frame(root, borderwidth=0, bg=bg_color)
screen_frame = Frame(root, borderwidth=0, bg=bg_color)
Mid_frame = Frame(root, borderwidth=0, bg=bg_color)

# Photo Header
image = Image.open("icon/icon.png")  # Opening the Image
photo = ImageTk.PhotoImage(image.resize((45, 45), Image.ANTIALIAS))

# Text Header
label = Label(
    main_frame,
    text="Calculator",
    font="Verdana 13 ",
    fg=fg_color,
    bg=bg_color,
    justify=CENTER,
)

# AOT BUTTON
label0 = Button(
    main_frame,
    image=photo,
    bg=bg_color,
    activebackground=bg_color,
    justify=CENTER,
    bd=0, cursor="hand2",
    command=aot,
)

# Radio Buttons for selecting theme
_variable = StringVar()
_variable.set(theme_name)

Themes = [content["Theme 1"]["Theme Name"], content["Theme 2"]["Theme Name"]]

for column_number, theme_ in enumerate(Themes):
    r = Radiobutton(
        main_frame, text=f"{theme_}",
        variable=_variable, value=theme_,
        bg=bg_color, fg=fg_color,
        cursor="hand2", selectcolor=radio_color,
        activeforeground=fg_color,
        activebackground=bg_color,
        indicatoron=True, command=theme,
    )
    r.grid(row=2, column=column_number)
    radio_list.append(r)

# Screen Of the calculator - Entry Widget
screen = Entry(
    screen_frame, relief=SUNKEN,
    bg=scrn_bg, fg=scrn_fg,
    selectbackground=scrn_sb,
    selectforeground=scrn_sf,
    borderwidth=1, justify=RIGHT,
    font="Ariel 30", cursor="arrow",
    insertbackground=scrn_cur)
screen.pack(side=TOP, pady=10, padx=10)

# Number Buttons
button_text = 1
for row_number in range(3, 0, -1):
    for column_number in range(3):
        o = Button(
            Mid_frame, text=f"{button_text}",
            width=b_width, padx=6,
            font=b_font, bd=b_border_width,
            bg=bg_color, fg=fg_color,
            activebackground=fg_color,
            activeforeground=bg_color,
            relief=b_relief, border=b_border)
        o.grid(row=row_number, column=column_number)
        button_text += 1
        widget_list0.append(o)

# Row Buttons
row_buttons = ["00", "0", "."]
for column_number, button_text in enumerate(row_buttons):
    o = Button(
        Mid_frame, text=f"{button_text}",
        width=b_width, padx=6,
        bg=bg_color, fg=fg_color,
        font=b_font, bd=b_border_width,
        activebackground=fg_color,
        activeforeground=bg_color,
        relief=b_relief, border=b_border)
    o.grid(row=4, column=column_number)
    widget_list0.append(o)

# Column Buttons
column_buttons = ["÷", "×", "-", "+"]
for row_number, button_text in enumerate(column_buttons):
    o = Button(
        Mid_frame, text=f"{button_text}",
        fg=aot_color,
        width=b_width, padx=6,
        bg=bg_color,
        font=b_font, bd=b_border_width,
        activeforeground=bg_color,
        relief=b_relief, border=b_border,
        activebackground=aot_color)
    o.grid(row=row_number, column=3)
    widget_list1.append(o)

# Few individual Buttons
equal_button = Button(
    Mid_frame, text="=",
    width=b_width, padx=6,
    font=b_font, bd=b_border_width,
    bg=bg_color, fg=aot_color,
    activebackground=aot_color,
    activeforeground=bg_color,
    relief=b_relief, border=b_border)

clear_button = Button(
    Mid_frame, text="⇐",
    width=b_width, padx=6,
    font=b_font, bd=b_border_width,
    bg=bg_color, fg=fg_color,
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief, border=b_border)

all_clear = Button(
    Mid_frame, text="C",
    width=b_width, padx=6,
    font=b_font, bd=b_border_width,
    bg=bg_color, fg=fg_color,
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief, border=b_border,
    command=lambda: screen.delete(0, END))

floor_division = Button(
    Mid_frame, text="%",
    width=b_width, padx=6,
    font=b_font, bd=b_border_width,
    bg=bg_color, fg=fg_color,
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief, border=b_border)

# Inserting into individual lists
widget_list0.append(floor_division)
widget_list0.append(clear_button)
widget_list1.append(equal_button)

# Packing Individual Buttons
equal_button.grid(row=4, column=3)
clear_button.grid(row=0, column=2)
floor_division.grid(row=0, column=1)
all_clear.grid(row=0, column=0)

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
label0.grid(row=0, column=0, columnspan=1)
label.grid(row=0, column=1, columnspan=2)

# Packing the frames

main_frame.pack(padx=0, pady=0)
screen_frame.pack(padx=0, pady=0)

##################################################################################################################

# Scientific Properties
sci_font = "ariel 15"
sci_width = 4

# Boolean Variables
sci_toggle = False
inv_toggle = False

# Button lists
sci_list = list()
sci_list2 = list()
inverted_list = list()


# some Scientific Functions - Deep Back End


# Function to toggle Scientific Calculator
def sci_cal():
    """Function to toggle the Scientific Calculator"""
    global sci_toggle

    # To Toggle On
    if not sci_toggle:
        mid_button.pack_forget()
        Mid_frame.pack_forget()

        all_clear.configure(height=1, width=4, font=sci_font)
        [
            widget.configure(height=1, width=4, font=sci_font)
            for widget in widget_list0 + widget_list1
        ]
        sci_frame.pack(padx=5, pady=0)

        mid_button.pack()
        Mid_frame.pack()

        sci_toggle = True

    # To Toggle Off
    elif sci_toggle:
        sci_frame.pack_forget()
        [
            widget.configure(height=1, width=b_width, font=b_font)
            for widget in widget_list0 + widget_list1
        ]
        all_clear.configure(height=1, width=b_width, font=b_font)

        sci_toggle = False


def sin(value):
    return math.sin(math.radians(float(value)))


def cos(value):
    return math.cos(math.radians(float(value)))


def tan(value):
    return math.tan(math.radians(float(value)))


def log(value):
    return math.log10(float(value))


def ln(value):
    return math.log(float(value))


def factorial(value):
    return math.factorial(int(value))


def square_root(value):
    return math.sqrt(float(value))


def calculate_sc(event):
    """Function to perform basic Scientific Calculations"""
    btn_text = event.widget["text"]
    expression = replace_(screen.get())
    answer = ""
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
    elif btn_text == "^":
        screen.insert(END, "^")
        return
    elif btn_text == "!":
        screen.insert(END, "!")
        return
    elif btn_text == "√x":
        screen.insert(END, "√")
        return
    elif btn_text == "(":
        screen.insert(END, "(")
        return
    elif btn_text == ")":
        screen.insert(END, ")")
        return
    elif btn_text == "π":
        screen.insert(END, "π")
        return
    elif btn_text == "e":
        screen.insert(END, "e")
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
    screen.delete(0, END)
    screen.insert(0, answer)


# Function to toggle Inverse
def inv():
    """Function to toggle Inverse"""
    global inv_toggle

    # To Toggle On
    if not inv_toggle:
        sci_upper_frame.pack_forget()
        sci_lower_frame.pack_forget()
        inverse_button.configure(bg=inv_color, fg=sci_fg,
                                 activebackground=inv_color,
                                 activeforeground=sci_fg)
        sci_upper_frame2.pack()
        sci_lower_frame.pack()
        inv_toggle = True

    # To Toggle Off
    elif inv_toggle:
        sci_upper_frame2.pack_forget()
        sci_lower_frame.pack_forget()

        sci_upper_frame.pack()
        sci_lower_frame.pack()
        inv_toggle = False


def asin(value):
    return math.degrees(math.asin(float(value)))


def acos(value):
    return math.degrees(math.acos(float(value)))


def atan(value):
    return math.degrees(math.atan(float(value)))


def exp(value):
    return math.exp(float(value))


# Function to perform inverse Scientific Calculations
def calculate_sc_inv(event):
    """Function to perform inverse Scientific Calculations"""
    btn_text = event.widget["text"]
    if btn_text == "sin⁻¹":
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
    elif btn_text == "10^":
        screen.insert(END, "10^")
        return


# Frames
sci_frame = Frame(root, bg=sci_bg)
sci_upper_frame = Frame(sci_frame, bg=sci_bg)
sci_upper_frame2 = Frame(sci_frame, bg=sci_bg)
sci_lower_frame = Frame(sci_frame, bg=sci_bg)
sci_upper_frame.pack()
sci_lower_frame.pack()
mid_button = Button(
    root, height=1, width=22,
    font=sci_font, cursor="hand2",
    activebackground=bg_color,
    activeforeground=fg_color,
    text="=", bd=0, command=sci_cal,
    bg=bg_color, fg=fg_color
)

# Advanced Common Scientific Buttons
button_list = ["sin", "cos", "tan", "log", "ln"]
for column_number, text in enumerate(button_list):
    o = Button(
        sci_upper_frame, text=f"{text}",
        width=sci_width,
        font=sci_font, bd=1,
        bg=sci_bg, fg=sci_fg,
        activebackground=sci_bg,
        activeforeground=sci_fg)
    o.grid(row=0, column=column_number)
    sci_list.append(o)

# Bottom row Buttons
i = 0
button_list2 = ["(", ")", "^", "√x", "!", "π", "e", " ", "RAD", "DEG"]
for row_number in range(2):
    for column_number in range(5):
        o = Button(
            sci_lower_frame, text=f"{button_list2[i]}",
            width=sci_width,
            bg=sci_bg, fg=sci_fg,
            font=sci_font, bd=1,
            activebackground=sci_bg,
            activeforeground=sci_fg)
        o.grid(row=row_number, column=column_number)
        sci_list2.append(o)
        i += 1

# Special Buttons
button_list_inverted = ["sin⁻¹", "cos⁻¹", "tan⁻¹", "10^", "eˣ"]
for column_number, text in enumerate(button_list_inverted):
    o = Button(sci_upper_frame2,
               text=f"{text}",
               width=sci_width,
               bg=sci_bg, fg=sci_fg,
               font=sci_font, bd=1,
               activebackground=sci_bg,
               activeforeground=sci_fg)

    o.grid(row=0, column=column_number)
    inverted_list.append(o)

# Individual Buttons
inverse_button = Button(sci_lower_frame,
                        text="INV", command=inv,
                        width=sci_width,
                        bg=sci_bg, fg=sci_fg,
                        font=sci_font, bd=1,
                        activebackground=sci_bg,
                        activeforeground=sci_fg)

# Packing Individual Buttons
inverse_button.grid(row=1, column=2)

# Binding Buttons
for button in inverted_list:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", calculate_sc_inv)

for button in sci_list + sci_list2:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", calculate_sc)

inverse_button.bind("<Enter>", change_on_hovering)
inverse_button.bind("<Leave>", return_on_hovering)

# mid_button.bind("<Enter>", change_on_hovering)
# mid_button.bind("<Leave>", return_on_hovering)

mid_button.pack()
Mid_frame.pack(padx=10, pady=0)

root.mainloop()
