from tkinter import *
from tkinter import ttk #used to style the widgets

# creating main tkinter window/toplevel
login_frame = Tk()

login_frame.geometry('215x100') # sets the size of the window
login_frame.title("Login Screen")  # set the title of the GUI window

# this will create a label widget
l1 = Label(login_frame, text="First:")
l1.pack(side=LEFT)

# entry widgets, used to take entry from user
e1 = Entry(login_frame)
e1.pack(side=LEFT)

btn1 = Button(login_frame, text="Button")
btn1.pack(side=LEFT)


mainloop()


def validate_login():
    pass
