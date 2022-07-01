import os

user_input = 0


def menu_options():
    global user_input
    user_input = int(input("What would you like to do?\n"
                           "1. View current working directory\n"
                           "2. Change current working directory\n"
                           "3. Bulk rename folders\n"
                           "4. Bulk rename folders and sub-folders\n"
                           "5. Create folders from Excel list of names\n"
                           "0. Exit\n"))
    call_menu_option()


def call_menu_option():
    print(user_input)
    match user_input:
        case 1:
            current_working_directory()
        case 2:
            change_current_working_directory()
        case 3 | 4 | 5:
            print("not an option yet")
        case 0:
            exit()


def change_current_working_directory():
    pass


def current_working_directory():
    pass


menu_options()