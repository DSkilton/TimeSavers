import os
import csv
from win32com.client import Dispatch

import Validation, MenuOptions, ViewAndChangeDirectory


def create_csv_file():
    file = open("template_with_headers.csv", "a")
    return file


def add_headers():
    create_csv_file()
    file = create_csv_file()

    # replace student name with nested list
    header = ["Student name", "Course name", "module names", "Number of assignments"]

    writer = csv.writer(create_csv_file())
    writer.writerow(header)


def open_excel_and_csv_file():
    excel_application = Dispatch("Excel.Application")
    excel_application.Visible = True

    workbook = excel_application.Workbooks\
        .Open(r""+ViewAndChangeDirectory.get_current_working_directory()
        .strip()+"\\template_with_headers.csv")


def add_header_to_csv_file():
    if create_csv_file():
        print("Found file")
    else:
        create_csv_file()
        print("Created file")

    user_input = str(input("Use default headers?"))

    if Validation.did_user_agree(user_input):
        print("adding headers")
        add_headers()

    user_input = str(input("header added. Would you like to open the file?"))

    if Validation.did_user_agree(user_input):
        open_excel_and_csv_file()


def create_folders_from_list():
    select_file()


def select_file():
    file_name = "student_names_and_courses.csv"
    header = ("student name", "module name", "assignments")

    for file in os.getcwd("."):
        if os.path.isfile(ViewAndChangeDirectory.get_current_working_directory().strip()+"\\student_names_and_courses.csv"):
            print("found csv files, " + file)
            break
    else:
        user_input = str(input("file does not exist, would you like it to be created?"))
        Validation.did_user_agree(user_input)

        if Validation.did_user_agree(user_input):
            create_csv_file()


def bulk_rename_folders():
    MenuOptions.bulk_operations_menu()


def bulk_rename_folders_and_sub_folders():
    MenuOptions.bulk_operations_menu()