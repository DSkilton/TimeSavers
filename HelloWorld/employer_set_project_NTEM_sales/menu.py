import tkinter
menu_count = 0

def display_menu():
    print("Welcome to NTEM Sales, select from the following options or 0. to exit")

    menu = {}
    menu['1'] = "Option 1"
    menu['2'] = "Option 2"
    menu['3'] = "Option 3"
    menu['0'] = "Exit"  # SystemExit

    menu_options = menu.keys()  # returns the dictionary keys
    sorted(menu_options) # sorts the dict keys
    menu_count = len(menu_options) #counts the size of menu_options

    for menu_option in menu_options:
        print(menu_option, menu[menu_option])

    print(menu_count)
    select_option()


def select_option():
    menu_choice = int(input("Please choose an option"))

    while menu_choice < menu_count:
        print("Here")

