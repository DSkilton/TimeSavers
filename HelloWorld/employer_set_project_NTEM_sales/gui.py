from tkinter import *

global login_frame


def login():
    username = entry_username.get()  # this stores the values from login_form textvariable=entry_username
    password = entry_password.get()  # this stores the values from login_form textvariable=entry_password

    if username == '' or password == '':
        label_message.set("Missing inputs")
    else:
        if username == "a" and password == "a":
            label_message.set("Login success")
        else:
            label_message.set("Wrong details")


def login_form():
    global entry_username  # using global var so info is accessible in login function
    global entry_password
    global label_message

    login_frame = Tk()
    entry_username = StringVar()  # StringVar() is a TKinter object used to manage Labels and Entrys
    entry_password = StringVar()
    label_message = StringVar()

    lbl_banner = Label(login_frame, text="Please enter details below", bg="orange", fg="white")
    lbl_username = Label(login_frame, text="Username:")
    lbl_password = Label(login_frame, text="Password:")
    lbl_message = Label(login_frame, text=" ", textvariable=label_message)
    entry_username = Entry(login_frame, textvariable=entry_username)
    entry_password = Entry(login_frame, textvariable=entry_password, show="*")
    btn_login = Button(login_frame, text="Login", command=login)

    # this will arrange the widgets
    lbl_banner.grid(row=0, column=0, columnspan=3, sticky=NS, pady=8)  # using columnspan to display text accross
    lbl_username.grid(row=1, column=0, sticky=E, pady=2)  # multiple cols
    lbl_password.grid(row=2, column=0, sticky=E, pady=2)
    entry_username.grid(row=1, column=1, sticky=W, pady=2)
    entry_password.grid(row=2, column=1, sticky=W, pady=4)
    btn_login.grid(row=4, column=1, sticky=W, pady=2)
    lbl_message.grid(row=5, column=0, sticky=NS, columnspan=2)
    mainloop()


login_form()


# Similar to above using pack
def pack_layout():
    login_frame.geometry('185x150')  # sets the size of the window
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
    btn1.grid(row=1, column=1, sticky=W, pady=2)
    mainloop()
