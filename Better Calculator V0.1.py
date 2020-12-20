"""
CHANGE LOG: Ver : 0.1
>> 20th December 2020
>> Added hover over widget feature
>> Added comments in the code
>> Added exclusive Zero Division Error output
>> Entry Widget Screen font made significantly smaller for better looks
>> Reduced Lot of unnecessary code
"""


from tkinter import *
from PIL import Image, ImageTk

# Common Properties
b_font = "ariel 30 bold"
b_relief = "groove"
b_border = 0
b_width = 2
b_borderwidth = 0

# Important Colours
bg_color, fg_color = "black", "white"

# For buttons having usual 'fg_color' foreground
widget_list0 = list()

# For buttons having exclusive 'cyan' foreground
widget_list1 = list()

# For exclusive radio buttons <Themes>
radio_list = list()


# some Functions - Back_end

# Function changes color of widgets hovering
def change_on_hovering(event):
    """Function changes color of widgets hovering"""
    button = event.widget
    button["bg"] = "grey"


# Function returns to normal color when not hovering
def return_on_hovering(event):
    """Function returns to normal color when not hovering"""
    button = event.widget
    button["bg"] = bg_color


# Function Changes theme from radio button input
def change_theme():
    """Function Changes Theme from radio button input"""
    # For Light Theme
    global bg_color, fg_color
    if _variable.get() == "Light Theme":
        bg_color = "white"
        fg_color = "black"
        root.configure(bg=bg_color)
        main_frame.configure(bg=bg_color)
        screen_frame.configure(bg=bg_color)
        label.configure(bg=bg_color, fg=fg_color)
        label0.configure(bg=bg_color, fg=fg_color)
        screen.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        for button in widget_list0:
            button.configure(bg=bg_color, fg=fg_color)

        for button in widget_list1:
            button.configure(bg=bg_color, fg="cyan", activebackground=bg_color)

        for radiobutton in radio_list:
            radiobutton.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)

    # For Dark Theme
    elif _variable.get() == "Dark Theme":
        bg_color = "black"
        fg_color = "white"
        root.configure(bg="Black")
        main_frame.configure(bg=bg_color)
        screen_frame.configure(bg=bg_color)
        label.configure(bg=bg_color, fg=fg_color)
        label0.configure(bg=bg_color, fg=fg_color)
        screen.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        for button in widget_list0:
            button.configure(bg=bg_color, fg=fg_color)

        for button in widget_list1:
            button.configure(bg=bg_color, fg="cyan")

        for radiobutton in radio_list:
            radiobutton.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)


# Function to execute Return Key in Screen (Entry Widget)
def enterclick(event):
    """Function to execute Return Key in Screen (Entry Widget)"""
    e = Event()
    e.widget = equal_button
    click(e)


# Function to execute click event of  all buttons
def click(event):
    widget = event.widget
    text = widget["text"]
    if text == "=":
        try:
            expression = screen.get()
            answer = eval(expression)
            screen.delete(0, END)
            screen.insert(0, answer)
        except ZeroDivisionError:
            print(ZeroDivisionError)
            screen.delete(0, END)
            screen.insert(0, "Can't Divide by Zero")
        except Exception as e:
            print(e)
            screen.delete(0, END)
            screen.insert(0, "Bad Expression")

        return

    elif text == "x":
        screen.insert(END, "*")
        return

    elif text == "<-":
        expression = screen.get()
        expression = expression[0 : len(expression) - 1]
        screen.delete(0, END)
        screen.insert(0, expression)
        return

    else:
        screen.insert(END, text)


# The Actual GUI - Front_End
root = Tk()  # Main window
root.geometry("295x550")  # Geometry

root.configure(bg=bg_color)  # Background of window
root.wm_iconbitmap("Cal_icon.ico")  # Icon of window


root.title("Calculator")  # Title Bar Name
root.resizable(height=0, width=0)  # Non Resizable window

main_frame = Frame(
    root, borderwidth=0, bg=bg_color
)  # First frame in Root window - Main_frame
screen_frame = Frame(
    root, borderwidth=0, bg=bg_color
)  # Second frame in Root window - Screen_frame
Mid_frame = Frame(
    root, borderwidth=0, bg=bg_color
)  # Third frame in Root window - Third_frame

# Photo Header
image = Image.open("Calculator.png")  # Opening the Image
photo = ImageTk.PhotoImage(
    image.resize((45, 45), Image.ANTIALIAS)
)  # Resizing the Image
label0 = Label(main_frame, image=photo, bg=bg_color, justify=CENTER)


# Text Header
label = Label(
    main_frame,
    text="Calculator",
    font="Verdana 13 ",
    fg=fg_color,
    bg=bg_color,
    justify=CENTER,
)


# Radio Buttons for selecting theme
_variable = StringVar()
_variable.set("Dark Theme")
Themes = ["Dark Theme", "Light Theme"]

for column_number, theme in enumerate(Themes):
    r = Radiobutton(
        main_frame,
        text=f"{theme}",
        variable=_variable,
        value=theme,
        bg=bg_color,
        fg="red",
        cursor="hand2",
        selectcolor="red",
        disabledforeground="red",
        indicatoron=True,
        activeforeground="red",
        activebackground=bg_color,
        command=change_theme,
    )
    r.grid(row=2, column=column_number)
    radio_list.append(r)

# Screen Of the calculator - Entry Widget
screen = Entry(
    screen_frame,
    bg=bg_color,
    foreground=fg_color,
    relief=SUNKEN,
    font="Ariel 30 ",
    cursor="arrow",
    selectbackground="#2C2B2C",
    selectforeground=fg_color,
    highlightcolor="red",
    highlightbackground="cyan",
    borderwidth=1,
    justify=RIGHT,
    insertbackground=fg_color,
)
screen.pack(side=TOP, pady=10, padx=10)


# Number Buttons
button_text = 1
for row in range(3, 0, -1):
    for column in range(3):
        a = Button(
            Mid_frame,
            text=f"{button_text}",
            border=b_border,
            padx=6,
            borderwidth=b_borderwidth,
            font=b_font,
            bg=bg_color,
            fg=fg_color,
            activebackground=fg_color,
            activeforeground=bg_color,
            relief=b_relief,
            width=b_width,
        )
        a.grid(row=row, column=column)
        button_text += 1
        widget_list0.append(a)

# Row Buttons
row_buttons = ["00", "0", "."]
for column_number, button_text in enumerate(row_buttons):
    b = Button(
        Mid_frame,
        text=f"{button_text}",
        border=b_border,
        padx=6,
        borderwidth=b_borderwidth,
        font=b_font,
        bg=bg_color,
        fg=fg_color,
        activebackground=fg_color,
        activeforeground=bg_color,
        relief=b_relief,
        width=b_width,
    )
    b.grid(row=4, column=column_number)
    widget_list0.append(b)

# Column Buttons
column_buttons = ["/", "x", "-", "+"]
for row_number, button_text in enumerate(column_buttons):
    c = Button(
        Mid_frame,
        text=f"{button_text}",
        border=b_border,
        padx=6,
        borderwidth=b_borderwidth,
        font=b_font,
        bg=bg_color,
        fg="cyan",
        activebackground="cyan",
        activeforeground=bg_color,
        relief=b_relief,
        width=b_width,
    )
    c.grid(row=row_number, column=3)
    widget_list1.append(c)

# Individual Buttons
equal_button = Button(
    Mid_frame,
    text="=",
    border=b_border,
    padx=6,
    borderwidth=b_borderwidth,
    font=b_font,
    bg=bg_color,
    fg="cyan",
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief,
    width=b_width,
)

clear_button = Button(
    Mid_frame,
    text="<-",
    border=b_border,
    padx=6,
    borderwidth=b_borderwidth,
    font=b_font,
    bg=bg_color,
    fg=fg_color,
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief,
    width=b_width,
)

all_clear = Button(
    Mid_frame,
    text=f"C",
    border=b_border,
    padx=6,
    borderwidth=b_borderwidth,
    font=b_font,
    bg=bg_color,
    fg=fg_color,
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief,
    width=b_width,
    command=lambda: screen.delete(0, END),
)

floor_division = Button(
    Mid_frame,
    text=f"%",
    border=b_border,
    padx=6,
    borderwidth=b_borderwidth,
    font=b_font,
    bg=bg_color,
    fg=fg_color,
    activebackground=fg_color,
    activeforeground=bg_color,
    relief=b_relief,
    width=b_width,
)

# Inserting into individual lists
widget_list0.append(all_clear)
widget_list0.append(floor_division)
widget_list0.append(clear_button)
widget_list1.append(equal_button)

# Packing Individual Buttons
equal_button.grid(row=4, column=3)
clear_button.grid(row=0, column=2)
floor_division.grid(row=0, column=1)
all_clear.grid(row=0, column=0)


# Binding all Buttons to necessary functions
for button in widget_list0:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", click)

for button in widget_list1:
    button.bind("<Enter>", change_on_hovering)
    button.bind("<Leave>", return_on_hovering)
    button.bind("<Button-1>", click)


# Binding the screen to Return Button
screen.bind("<Return>", enterclick)

# Packing the labels
label0.grid(row=0, column=0, columnspan=1)
label.grid(row=0, column=1, columnspan=2)

# Packing the frames
main_frame.pack(padx=0, pady=0)
screen_frame.pack(padx=0, pady=0)
Mid_frame.pack(padx=10, pady=0)

root.mainloop()
