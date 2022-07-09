import csv
import os

import course_details
import folder_operations


def to_refactor():
    name = ""
    course = ""
    list_of_names = []

    with open("template_with_headers.csv", "r") as read_only:
        csv_object = csv.reader(read_only)
        next(csv_object)

        for line in csv_object:
            name = line[0]
            list_of_names.append(name)
            name += line[0]
            course += line[1]

            os.mkdir(course)
            os.chdir(course)

            for module in course_details.BTEC_LVL3_YR1:
                os.mkdir(module)

                for student_name in list_of_names:
                    os.mkdir(student_name)




to_refactor()
