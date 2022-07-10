import csv
import fnmatch
import os
from pathlib import Path
import pandas as pd
import MenuOptions

user_input = 0





def create_folders_from_list():
    select_file()


def didUserAgree(str_input):
    pass


def createFileWithHeader():
    pass


def select_file():
    file_name = "student_names_and_courses.csv"
    header = ("student name", "module name", "assignments")

    for file in os.getcwd("."):
        if os.path.isfile("C:\\Users\MC03353\\PycharmProjects\\ABitOfEverything\\student_names_and_courses.csv"):
            print("found csv files, " + file)
            break
    else:
        user_input = str(input("file does not exist, would you like it to be created?"))
        didUserAgree(user_input)

        if didUserAgree():
            createFileWithHeader()


def bulk_rename_folders():
    MenuOptions.bulk_operations_menu()


def bulk_rename_folders_and_sub_folders():
    MenuOptions.bulk_operations_menu()





MenuOptions.top_level_menu_options()
