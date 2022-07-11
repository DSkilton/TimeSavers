import csv
import os

from win32com.client import Dispatch

import MenuOptions
import Validation
import ViewAndChangeDirectory


def create_csv_file():
    file = open("template_with_headers.csv", "a")
    return file


def check_if_headers_exist():
    print("Just checking the file...")
    file = open("template_with_headers.csv", "r")

    line = file.read().splitlines()

    # while line:
    print(line)

    # this needs fixing, theows error
    data = line.split(",")

    if str(data[0]) == "Student name" and str(data[1]) == "Course name" and str(data[2]) == "Module names" and str(data[3]) == "Number of assignments":
        print("found headers")

    # line = file.readline()
    return data


def add_headers():
    header = ["Student name", "Course name", "module names", "Number of assignments"]

    create_csv_file()
    file = create_csv_file()

    print("head" + str(check_if_headers_exist()))

    # replace student name with nested list
    writer = csv.writer(create_csv_file())
    writer.writerow(header)


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


def create_folders_from_list():
    select_file()


def select_file():
    file_name = "template_with_headers.csv"
    header = ("student name", "module name", "assignments")

    for file in os.getcwd("."):
        if os.path.isfile(ViewAndChangeDirectory.get_current_working_directory()
                                  .strip() + "\\template_with_headers.csv.csv"):
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
