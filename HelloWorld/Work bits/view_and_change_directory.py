import os
import menu_options


def change_current_working_directory():
    new_working_directory = str(input("Below, paste the directory you would like to change to:"))

    if len(new_working_directory) == 0:
        print("directory not changed")
    else:
        print("You have changed to:" + '"' + new_working_directory + '"')
    MenuOptions.top_level_menu_options()


def get_current_working_directory():
    return os.getcwd()


def current_working_directory():
    cwd = os.getcwd()
    print("Current working director is: {0}".format(cwd))
    MenuOptions.top_level_menu_options()
