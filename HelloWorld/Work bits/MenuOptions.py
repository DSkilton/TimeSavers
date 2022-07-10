import ViewAndChangeDirectory, FolderOperations


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
            ViewAndChangeDirectory.current_working_directory()
        case 2:
            ViewAndChangeDirectory.change_current_working_directory()
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
            FolderOperations.create_folders_from_list()
        case 2:
            FolderOperations.bulk_rename_folders()
        case 3:
            FolderOperations.bulk_rename_folders_and_sub_folders()
        case 0:
            top_level_menu_options()
        case _:
            print("no such option, try again")