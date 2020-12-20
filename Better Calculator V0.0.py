"""
CHANGE LOG: Ver : 0.0
>> 19th December 2020
>> Starting with the basics
>> Added 2 themes

Known Issues
>> Radio Button does'nt show theme initially
"""
from tkinter import *

from PIL import Image, ImageTk

# Button properties
b_font = "ariel 30 bold"
b_relief = "groove"
b_border = 0
b_width = 2
b_borderwidth = 0
bg_color = "black"
fg_color = "white"


# some Functions

def ChangeTheme():
    global bg_color, fg_color
    if v.get() == "Light Theme":
        bg_color = "white"
        fg_color = "black"
        root.configure(bg="white")
        main_frame.configure(bg=bg_color)
        label.configure(bg=bg_color, fg=fg_color)
        label0.configure(bg=bg_color, fg=fg_color)
        screen.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        for button in widget_list0:
            button.configure(bg=bg_color, fg=fg_color)

        for button in widget_list1:
            button.configure(bg=bg_color, fg="cyan", activebackground=bg_color)

        for radiobutton in radio_list:
            radiobutton.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)

    elif v.get() == "Dark Theme":
        bg_color = "black"
        fg_color = "white"
        root.configure(bg="Black")
        main_frame.configure(bg=bg_color, )
        label.configure(bg=bg_color, fg=fg_color)
        label0.configure(bg=bg_color, fg=fg_color)
        screen.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        for button in widget_list0:
            button.configure(bg=bg_color, fg=fg_color)

        for button in widget_list1:
            button.configure(bg=bg_color, fg="cyan")

        for radiobutton in radio_list:
            radiobutton.configure(bg=bg_color, fg=fg_color, activebackground=bg_color)


def enterclick(event):
    e = Event()
    e.widget = equal_button
    click(e)


def clear():
    expression = screen.get()
    expression = expression[0: len(expression) - 1]
    screen.delete(0, END)
    screen.insert(0, expression)


ac = lambda: screen.delete(0, END)


def click(event):
    button = event.widget
    text = button["text"]
    if text == "=":
        try:
            expression = screen.get()
            answer = eval(expression)
            screen.delete(0, END)
            screen.insert(0, answer)
        except Exception as e:
            error = e
            screen.delete(0, END)
            screen.insert(0, "Error")
        return
    if text == "x":
        screen.insert(END, "*")
        return
    screen.insert(END, text)


root = Tk()

root.geometry("295x550")



root.configure(bg=bg_color)
root.wm_iconbitmap("Cal_icon.ico")


root.title("Calculator")
# root.resizable(height=0, width=0)

main_frame = Frame(root, borderwidth=0, bg=bg_color)
main_frame.pack(padx=0, pady=0)

# Label Image
image = Image.open("Calculator.png")
_image = image.resize((45, 45), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(_image)
label0 = Label(main_frame, image=photo, bg=bg_color, justify=CENTER)
label0.grid(row=0, column=0, columnspan=1)

label = Label(main_frame, text="Calculator", font="Verdana 13 ", fg=fg_color, bg=bg_color, justify=CENTER)
label.grid(row=0, column=1, columnspan=2)
# Radio Buttons
v = StringVar()
v.set("Dark Theme")

Themes = ["Dark Theme",
          "Light Theme"]
widget_list0, widget_list1, radio_list = list(), list(), list()
for column_number, theme in enumerate(Themes):
    a = Radiobutton(main_frame, text=f"{theme}", variable=v, value=theme,
                    bg=bg_color, fg="red", cursor="hand2", selectcolor="red",
                    disabledforeground="red", indicatoron=True,
                    activeforeground="red", activebackground=bg_color,
                    command=ChangeTheme)
    a.grid(row=2, column=column_number)
    radio_list.append(a)

screen = Entry(root, bg=bg_color, foreground=fg_color, relief=SUNKEN, font="Ariel 45 ", cursor="arrow",
               selectbackground="#2C2B2C", selectforeground=fg_color, highlightcolor="red",
               highlightbackground="cyan", borderwidth=1, justify=RIGHT,
               insertbackground=fg_color)
screen.pack(side=TOP, pady=10, padx=10)
screen.bind("<Return>", enterclick)

Mid_frame = Frame(root)
Mid_frame.pack(padx=10, pady=0)

# Number Buttons
button_text = 1
for row in range(3, 0, -1):
    for column in range(3):
        a = Button(Mid_frame, text=f"{button_text}", border=b_border, padx=6,
                   borderwidth=b_borderwidth, font=b_font,
                   bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                   relief=b_relief, width=b_width)
        a.grid(row=row, column=column)
        a.bind("<Button-1>", click)
        button_text += 1
        widget_list0.append(a)

# Row Buttons
row_buttons = ["00", "0", "."]
for column_number, button_text in enumerate(row_buttons):
    b = Button(Mid_frame, text=f"{button_text}", border=b_border, padx=6,
               borderwidth=b_borderwidth, font=b_font,
               bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
               relief=b_relief, width=b_width)
    b.grid(row=4, column=column_number)
    b.bind("<Button-1>", click)
    widget_list0.append(b)

# Column Buttons
column_buttons = ["/", "x", "-", "+"]
for row_number, button_text in enumerate(column_buttons):
    c = Button(Mid_frame, text=f"{button_text}", border=b_border, padx=6,
               borderwidth=b_borderwidth, font=b_font,
               bg=bg_color, fg="cyan", activebackground="cyan", activeforeground=bg_color,
               relief=b_relief, width=b_width)
    c.grid(row=row_number, column=3)
    c.bind("<Button-1>", click)
    widget_list1.append(c)

# Individual Buttons
equal_button = Button(Mid_frame, text="=", border=b_border, padx=6,
                      borderwidth=b_borderwidth, font=b_font,
                      bg=bg_color, fg="cyan", activebackground=fg_color, activeforeground=bg_color,
                      relief=b_relief, width=b_width)

clear_button = Button(Mid_frame, text="<-", border=b_border, padx=6,
                      borderwidth=b_borderwidth, font=b_font,
                      bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                      relief=b_relief, width=b_width, command=clear)

all_clear = Button(Mid_frame, text=f"C", border=b_border, padx=6,
                   borderwidth=b_borderwidth, font=b_font,
                   bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                   relief=b_relief, width=b_width, command=ac)

floor_division = Button(Mid_frame, text=f"%", border=b_border, padx=6,
                        borderwidth=b_borderwidth, font=b_font,
                        bg=bg_color, fg=fg_color, activebackground=fg_color, activeforeground=bg_color,
                        relief=b_relief, width=b_width)

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

# Binding Individual Buttons
all_clear.bind('<Button-1>', click)
equal_button.bind('<Button-1>', click)
floor_division.bind('<Button-1>', click)

root.mainloop()
