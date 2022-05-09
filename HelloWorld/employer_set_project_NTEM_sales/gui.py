from tkinter import *
from tkinter import ttk #used to style the widgets

# creating main tkinter window/toplevel
login_frame = Tk()


def pack_layou():
    login_frame.geometry('185x150') # sets the size of the window
    login_frame.title("Login Screen")  # set the title of the GUI window

    # this will create a label widget
    l1 = Label(login_frame, text="First:")
    btn1 = Button(login_frame, text="Button")

    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row=0, column=0, sticky=W, pady=2)

    # entry widgets, used to take entry from user
    e1 = Entry(login_frame)

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    btn1.grid(row=1, column= 1, sticky=W, pady=2)
    mainloop()


def grid_layout():
    # this will create a label widget
    l1 = Label(login_frame, text="First:")
    btn1 = Button(login_frame, text="Button")

    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row=0, column=0, sticky=W, pady=2)

    # entry widgets, used to take entry from user
    e1 = Entry(login_frame)

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    btn1.grid(row=1, column=1, sticky=W, pady=2)
    mainloop()


def validate_login():
    pass
