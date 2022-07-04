import csv
import fnmatch
import os
import pandas as pd

user_input = 0


def top_level_menu_options():
    global user_input
    user_input = int(input("What would you like to do?\n"
                           "1. View current working directory\n"
                           "2. Change current working directory\n"
                           "3. Bulk operations menu\n"
                           "0. Exit\n"))
    top_level_menu_match()


def top_level_menu_match():
    match user_input:
        case 1:
            current_working_directory()
        case 2:
            change_current_working_directory()
        case 3:
            bulk_operations_menu()
        case 0:
            exit()
        case _:
            print("no such option, try again")


def bulk_operations_menu():
    global user_input
    user_input = int(input("1. Create folders from csv or tsv of names\n"
                           "2. Bulk rename folders\n"
                           "3. Bulk rename folders and sub-folders\n"
                           "0. Up a menu\n"))
    bulk_operations_menu_match()


def bulk_operations_menu_match():
    match user_input:
        case 1:
            create_folders_from_list()
        case 2:
            bulk_rename_folders()
        case 3:
            bulk_rename_folders_and_sub_folders()
        case 0:
            top_level_menu_options()
        case _:
            print("no such option, try again")


def create_folders_from_list():
    select_file()


def select_file():
    file_name = "student_names_and_courses.csv"
    header = ("student name", "module name", "assignments")

    for file in os.listdir("."):
        if os.path.isfile("C:\\Users\MC03353\\PycharmProjects\\ABitOfEverything\\student_names_and_courses.csv"):
            print("found csv files")
            break
    else:
        print("file does not exist")




def bulk_rename_folders():
    bulk_operations_menu()


def bulk_rename_folders_and_sub_folders():
    bulk_operations_menu()


def change_current_working_directory():
    new_working_directory = str(input("Below, paste the directory you would like to change to:"))
    print("You have changed to:" + '"' + new_working_directory + '"')
    top_level_menu_options()


def current_working_directory():
    cwd = os.getcwd()
    print("Current working director is: {0}".format(cwd))
    top_level_menu_options()


top_level_menu_options()
