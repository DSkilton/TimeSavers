import csv
import os

from win32com.client import Dispatch

import MenuOptions
import Validation
import ViewAndChangeDirectory


def create_csv_file():
    file = open("template_with_headers.csv", "w")
    return file


def check_if_headers_exist():
    print("Just checking the file...")
    file = open("template_with_headers.csv", "r")

    line = file.read().splitlines()

    # while line:
    print(line)

    if len(line) != 0:
        for element in line:
            data = element.split(",")

        if str(data[0]) == "Student name" and str(data[1]) == "Course name" and str(data[2]) == "Module names" and str(data[3]) == "Number of assignments":
            print("found headers")
            return True
    else:
        return False


def add_headers():
    header = ["Student name", "Course name", "module names", "Number of assignments"]

    create_csv_file()
    file = create_csv_file()

    if check_if_headers_exist():
        print("headers exist " + str(check_if_headers_exist()))

    else:
        # replace student name with nested list
        writer = csv.writer(create_csv_file())
        writer.writerow(header)
        print("headers added to file")


def open_excel_and_csv_file():
    excel_application = Dispatch("Excel.Application")
    excel_application.Visible = True

    workbook = excel_application.Workbooks.Open(r"" + ViewAndChangeDirectory.get_current_working_directory()
                                                .strip() + "\\template_with_headers.csv")


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

    MenuOptions.top_level_menu_options()


def create_folders_from_list():
    select_file()


def load_file_to_list():
    with open("template_with_headers.csv", "r") as read_only:
        print("should be printing file")
        print(read_only.readline())

    MenuOptions.bulk_operations_menu()


def select_file():

    # This needs to search the current directory for template_with_headers
    # if it is found, load file into list
    # if it is not found, create it and ask user if they want to open the file

    # if the loaded information is correct, ask user to create folder structure for that student
    # the course they are on will dictate what unit folders are created and which assignment folders

    # last prompt is to ask user if they want to go to the new directories they created to
     
    if create_csv_file():
        print("found file")
    else:
        create_csv_file()
        print("file created")

    add_header_to_csv_file()
    load_file_to_list()
    print("finished function")


def bulk_rename_folders():
    MenuOptions.bulk_operations_menu()


def bulk_rename_folders_and_sub_folders():
    MenuOptions.bulk_operations_menu()
