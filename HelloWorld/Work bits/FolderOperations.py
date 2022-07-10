import os

import Validation
import MenuOptions


def create_file_with_header():
    pass


def create_folders_from_list():
    select_file()


def select_file():
    file_name = "student_names_and_courses.csv"
    header = ("student name", "module name", "assignments")

    for file in os.getcwd("."):
        if os.path.isfile("C:\\Users\MC03353\\PycharmProjects\\ABitOfEverything\\student_names_and_courses.csv"):
            print("found csv files, " + file)
            break
    else:
        user_input = str(input("file does not exist, would you like it to be created?"))
        Validation.did_user_agree(user_input)

        if Validation.did_user_agree():
            create_file_with_header()


def bulk_rename_folders():
    MenuOptions.bulk_operations_menu()


def bulk_rename_folders_and_sub_folders():
    MenuOptions.bulk_operations_menu()