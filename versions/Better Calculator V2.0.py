"""
CHANGE LOG: Ver : 2.0
>> 27th December 2020
>> Optimised backend
>> Reduced Code
>> Fixed bugs

"""

from tkinter import *
from PIL import Image, ImageTk
import math
# Special Colors

sci_bg, sci_fg = 'grey', 'white'
bg_color, fg_color = "black", "white"
dark_grey = '#3B3E3F'
mint, dark_mint = '#15CA9C', '#177351'
blue, dark_blue = '#32CAC9', '#299493'
hover, hover_inverse = '#3B3E3F', dark_mint
inv_color = mint
aot_color = "cyan"

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
widget_list1 = list()  # For buttons having exclusive 'cyan' foreground
radio_list = list()    # For exclusive radio buttons <Themes>


# some Functions - Front_end


# To Keep window always on top
def aot():
    """To Keep window always on top"""
    global aot_toggle

    # To Toggle On
    if not aot_toggle:
        root.attributes('-topmost', True)
        label['fg'] = aot_color
        label['font'] = 'Verdana 12 italic'
        aot_toggle = True

    # To Toggle Off
    else:
        root.attributes('-topmost', False)
        label['fg'] = fg_color
        label['font'] = 'Verdana 13'
        aot_toggle = False


# Function Changes theme from radio button input
def change_theme():
    """Function Changes Theme from radio button input"""
    global bg_color, fg_color, sci_bg, hover, inv_color, hover_inverse, aot_color

    # For Light Theme
    if _variable.get() == "Light Theme":
        # Theme Colors
        sci_bg = dark_grey
        bg_color, fg_color = "white", "black"
        hover, hover_inverse = 'grey', dark_blue
        inv_color = blue
        aot_color = 'red'

        root.configure(bg=bg_color)
        label0.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)

        label.configure(bg=bg_color, fg=aot_color) if aot_toggle else label.configure(bg=bg_color, fg=fg_color)

        sci_upper_frame.configure(bg=sci_bg)
        main_frame.configure(bg=bg_color)
        screen_frame.configure(bg=bg_color)

        screen.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)

        mid_button.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, activeforeground=fg_color)

        [widget.configure(bg=dark_grey) for widget in inverted_list]

        [widget.configure(bg=dark_grey) for widget in sci_list]

        [widget.configure(bg=dark_grey) for widget in sci_list2]

        inverse_button.configure(bg=inv_color) if inv_toggle else inverse_button.configure(bg=sci_bg)

        for radiobutton in radio_list:
            radiobutton.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, selectcolor="cyan")

        for widget in widget_list0:
            widget.configure(bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color, )

        for widget in widget_list1:
            widget.configure(bg=bg_color, fg="red", activebackground='red', activeforeground=bg_color, )

        all_clear.configure(bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color, )

    # For Dark Theme
    elif _variable.get() == "Dark Theme":
        # Theme Colors
        sci_bg = "grey"
        bg_color, fg_color = "black", "white"
        hover, hover_inverse = dark_grey, dark_mint
        inv_color = mint
        aot_color = 'cyan'

        root.configure(bg=bg_color)
        label0.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)

        label.configure(bg=bg_color, fg=aot_color) if aot_toggle else label.configure(bg=bg_color, fg=fg_color)

        sci_upper_frame.configure(bg=sci_bg)
        main_frame.configure(bg=bg_color)
        screen_frame.configure(bg=bg_color)

        screen.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)

        mid_button.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, activeforeground=fg_color)

        [widget.configure(bg=sci_bg) for widget in inverted_list]

        [widget.configure(bg=sci_bg) for widget in sci_list]

        [widget.configure(bg=sci_bg) for widget in sci_list2]

        inverse_button.configure(bg=inv_color) if inv_toggle else inverse_button.configure(bg=sci_bg)

        for radiobutton in radio_list:
            radiobutton.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, selectcolor="red")

        for widget in widget_list0:
            widget.configure(bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color, )

        for widget in widget_list1:
            widget.configure(bg=bg_color, fg="cyan", activebackground='cyan', activeforeground=bg_color)

        all_clear.configure(bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color)


# Function changes color of widgets hovering
def change_on_hovering(event):
    """Function changes color of widgets hovering"""
    widget = event.widget
    parent = event.widget.winfo_parent()
    # print(parent)
    if parent in ['.!frame4.!frame', '.!frame4.!frame2', '.!frame4.!frame3']:
        if widget['text'] == 'INV':
            widget.configure(bg=hover_inverse) if inv_toggle else widget.configure(bg=hover)
            return
        else:
            widget.configure(bg=hover)
        return
    widget['bg'] = 'grey'


# Function returns to normal color when not hovering
def return_on_hovering(event):
    """Function returns to original color when not hovering"""
    widget = event.widget
    parent = event.widget.winfo_parent()
    if parent in ['.!frame4.!frame', '.!frame4.!frame2', '.!frame4.!frame3']:
        if widget['text'] == 'INV':
            widget.configure(bg=inv_color) if inv_toggle else widget.configure(bg=sci_bg)
            return
        else:
            widget.configure(bg=sci_bg)
        return
    widget['bg'] = bg_color


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
            screen.insert(0, 'Invalid Input')
        except TypeError:
            screen.delete(0, END)
            screen.insert(0, 'No Input')
        return

    elif btn_text == "<-":
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
    expression = expression.replace('x', '*')
    expression = expression.replace('÷', '/')
    expression = expression.replace('^', "**")
    expression = expression.replace('π', str(math.pi))
    expression = expression.replace('e', str(math.e))
    expression = expression.replace('sin⁻¹(', "asin(")
    expression = expression.replace('cos⁻¹(', "acos(")
    expression = expression.replace('tan⁻¹(', "atan(")
    expression = expression.replace('!', 'factorial(')
    expression = expression.replace("√", "square_root(")
    
    # Adding required parenthesis
    if expression.count('(') > expression.count(')'):
        expression = expression + ')'
    
    # Removing Redundant parenthesis
    while expression.count('(') < expression.count(')'):
        expl = list(expression)
        expl.remove(')')
        expression = ''.join(expl)
    return expression


# The Actual GUI - Front_End

root = Tk()                             # Main window
root.geometry("267x500")                # Geometry

root.configure(bg=bg_color)             # Background of window
root.wm_iconbitmap("Cal_icon.ico")      # Icon of window

root.title("Calculator")                # Title Bar Name
root.resizable(height=0, width=0)       # Non Resizable window

# Frames
main_frame = Frame(root, borderwidth=0, bg=bg_color)    # First frame in Root window - Main_frame
screen_frame = Frame(root, borderwidth=0, bg=bg_color)  # Second frame in Root window - Screen_frame
Mid_frame = Frame(root, borderwidth=0, bg=bg_color)     # Third frame in Root window - Mid_frame


# Photo Header
image = Image.open("Calculator.png")                                 # Opening the Image
photo = ImageTk.PhotoImage(image.resize((45, 45), Image.ANTIALIAS))  # Resizing the Image
label0 = Button(main_frame, image=photo, bg=bg_color,
                activebackground=bg_color, justify=CENTER, bd=0, command=aot)

# Text Header
label = Label(main_frame, text="Calculator", font="Verdana 13 ", fg=fg_color, bg=bg_color, justify=CENTER)

# Radio Buttons for selecting theme
_variable = StringVar()
_variable.set("Dark Theme")

Themes = ["Dark Theme", "Light Theme"]

for column_number, theme in enumerate(Themes):
    r = Radiobutton(main_frame, text=f"{theme}", variable=_variable, value=theme,
                    bg=bg_color, fg="red", cursor="hand2", selectcolor="red",
                    disabledforeground="red", indicatoron=True,
                    activeforeground="red", activebackground=bg_color,
                    command=change_theme)
    r.grid(row=2, column=column_number)
    radio_list.append(r)

# Screen Of the calculator - Entry Widget
screen = Entry(screen_frame, bg=bg_color, foreground=fg_color, relief=SUNKEN, font="Ariel 30 ",
               cursor="arrow", selectbackground="#2C2B2C", selectforeground=fg_color,
               highlightcolor="red", highlightbackground="cyan",
               borderwidth=1, justify=RIGHT, insertbackground=fg_color)
screen.pack(side=TOP, pady=10, padx=10)

# Number Buttons
button_text = 1
for row_number in range(3, 0, -1):
    for column_number in range(3):
        a = Button(Mid_frame, text=f"{button_text}", border=b_border, padx=6,
                   bd=b_border_width, font=b_font,
                   bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                   relief=b_relief, width=b_width)
        a.grid(row=row_number, column=column_number)
        button_text += 1
        widget_list0.append(a)

# Row Buttons
row_buttons = ["00", "0", "."]
for column_number, button_text in enumerate(row_buttons):
    b = Button(Mid_frame, text=f"{button_text}", border=b_border, padx=6,
               borderwidth=b_border_width, font=b_font,
               bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
               relief=b_relief, width=b_width)
    b.grid(row=4, column=column_number)
    widget_list0.append(b)

# Column Buttons
column_buttons = ["÷", "x", "-", "+"]
for row_number, button_text in enumerate(column_buttons):
    c = Button(Mid_frame, text=f"{button_text}", border=b_border, padx=6,
               borderwidth=b_border_width, font=b_font,
               bg=bg_color, fg="cyan", activebackground="cyan", activeforeground=bg_color,
               relief=b_relief, width=b_width)
    c.grid(row=row_number, column=3)
    widget_list1.append(c)

# Few individual Buttons
equal_button = Button(Mid_frame, text="=", border=b_border, padx=6, borderwidth=b_border_width, font=b_font,
                      bg=bg_color, fg="cyan", activebackground="cyan", activeforeground=bg_color,
                      relief=b_relief, width=b_width)

clear_button = Button(Mid_frame, text="<-", border=b_border, padx=6, borderwidth=b_border_width, font=b_font,
                      bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                      relief=b_relief, width=b_width)

all_clear = Button(Mid_frame, text="C", border=b_border, padx=6, borderwidth=b_border_width, font=b_font,
                   bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                   relief=b_relief, width=b_width, command=lambda: screen.delete(0, END))

floor_division = Button(Mid_frame, text="%", border=b_border, padx=6, borderwidth=b_border_width, font=b_font,
                        bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                        relief=b_relief, width=b_width)

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
for button in (widget_list0+widget_list1):
    button.bind('<Enter>', change_on_hovering)
    button.bind('<Leave>', return_on_hovering)
    button.bind('<Button-1>', click)


all_clear.bind('<Enter>', change_on_hovering)
all_clear.bind('<Leave>', return_on_hovering)


# Binding more Button
screen.bind("<Return>", enter_click)
all_clear.bind('<Enter>', change_on_hovering)
all_clear.bind('<Leave>', return_on_hovering)


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
        [widget.configure(height=1, width=4, font=sci_font) for widget in widget_list0]
        all_clear.configure(height=1, width=4, font=sci_font)
        [widget.configure(height=1, width=4, font=sci_font) for widget in widget_list1]
        sci_frame.pack(padx=5, pady=0)
        mid_button.pack()
        Mid_frame.pack()
        sci_toggle = True

    # To Toggle Off
    elif sci_toggle:
        sci_frame.pack_forget()
        [widget.configure(height=1, width=b_width, font=b_font) for widget in widget_list0]
        all_clear.configure(height=1, width=b_width, font=b_font)
        [widget.configure(height=1, width=b_width, font=b_font) for widget in widget_list1]
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


# Function to perform basic Scientific Calculations
def calculate_sc(event):
    """Function to perform basic Scientific Calculations"""
    btn_text = event.widget['text']
    expression = replace_(screen.get())
    answer = ''
    if btn_text == 'sin':
        screen.insert(END, "sin(")
        return
    elif btn_text == 'cos':
        screen.insert(END, "cos(")
        return
    elif btn_text == 'tan':
        screen.insert(END, "tan(")
        return
    elif btn_text == 'log':
        screen.insert(END, "log(")
        return
    elif btn_text == 'ln':
        screen.insert(END, "ln(")
        return
    elif btn_text == '^':
        screen.insert(END, "^")
        return
    elif btn_text == '!':
        screen.insert(END, "!")
        return
    elif btn_text == '√x':
        screen.insert(END, "√")
        return
    elif btn_text == '(':
        screen.insert(END, '(')
        return
    elif btn_text == ')':
        screen.insert(END, ')')
        return
    elif btn_text == 'π':
        screen.insert(END, "π")
        return
    elif btn_text == 'e':
        screen.insert(END, "e")
        return
    elif btn_text == 'DEG':
        try:
            answer = str(math.degrees(float(expression)))
        except ValueError:
            screen.delete(0, END)
            screen.insert(0, "Value Error")
            return
    elif btn_text == 'RAD':
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
        inverse_button.configure(bg=inv_color)
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
    btn_text = event.widget['text']
    if btn_text == 'sin⁻¹':
        screen.insert(END, "sin⁻¹(")
        return
    elif btn_text == 'cos⁻¹':
        screen.insert(END, "cos⁻¹(")
        return
    elif btn_text == 'tan⁻¹':
        screen.insert(END, "tan⁻¹(")
        return
    elif btn_text == 'eˣ':
        screen.insert(END, "exp(")
        return
    elif btn_text == '10^':
        screen.insert(END, "10^")
        return


# Frames
sci_frame = Frame(root, bg=sci_bg)
sci_upper_frame = Frame(sci_frame, bg=sci_bg)
sci_upper_frame2 = Frame(sci_frame, bg=sci_bg)
sci_lower_frame = Frame(sci_frame, bg=sci_bg)
sci_upper_frame.pack()
sci_lower_frame.pack()
mid_button = Button(root, height=1, width=1,
                    font=sci_font, cursor="hand2", activebackground=bg_color, activeforeground=fg_color,
                    text='=', bd=0, bg=bg_color, fg=fg_color, command=sci_cal)

# Advanced Common Scientific Buttons
button_list = ['sin', 'cos', 'tan', 'log', 'ln']
for column_number, text in enumerate(button_list):
    o = Button(sci_upper_frame, text=f'{text}',
               font=sci_font, width=sci_width,
               bg=sci_bg, bd=1, fg=sci_fg, activebackground=sci_bg, activeforeground=sci_fg)
    o.grid(row=0, column=column_number)
    sci_list.append(o)

# Bottom row Buttons
i = 0
button_list2 = ['(', ')', '^', '√x', '!', 'π', 'e', ' ', 'RAD', 'DEG']
for row_number in range(2):
    for column_number in range(5):
        o = Button(sci_lower_frame, text=f'{button_list2[i]}',
                   font=sci_font, width=sci_width,
                   bg=sci_bg, bd=1, fg=sci_fg, activebackground=sci_bg, activeforeground=sci_fg)
        o.grid(row=row_number, column=column_number,)
        sci_list2.append(o)
        i += 1

# Special Buttons
button_list_inverted = ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', '10^', 'eˣ']
for column_number, text in enumerate(button_list_inverted):
    o = Button(sci_upper_frame2, text=f'{text}',
               font=sci_font, width=sci_width,
               bg=sci_bg, bd=1, fg=sci_fg, activebackground=sci_bg, activeforeground=sci_fg)
    o.grid(row=0, column=column_number)
    inverted_list.append(o)

# Individual Buttons
inverse_button = Button(sci_lower_frame, text='INV', font=sci_font, width=sci_width,
                        bg=sci_bg, bd=1, fg=sci_fg, activebackground=sci_bg,
                        activeforeground=sci_fg, command=inv)

# Packing Individual Buttons
inverse_button.grid(row=1, column=2)

# Binding Buttons
for button in inverted_list:
    button.bind('<Enter>', change_on_hovering)
    button.bind('<Leave>', return_on_hovering)
    button.bind('<Button-1>', calculate_sc_inv)

for button in (sci_list+sci_list2):
    button.bind('<Enter>', change_on_hovering)
    button.bind('<Leave>', return_on_hovering)
    button.bind('<Button-1>', calculate_sc)

inverse_button.bind('<Enter>', change_on_hovering)
inverse_button.bind('<Leave>', return_on_hovering)

mid_button.pack()
Mid_frame.pack(padx=10, pady=0)


root.mainloop()
