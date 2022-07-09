import json
import requests
import os
from pathlib import Path

#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#jobs = json.loads(response.text)

#for task in jobs:
    #print(task)

# entries = Path()
# for entry in entries.iterdir():
#     print(entry.name)
#
# dir2 = os.pathlib.Path.iterdir()
# directory = os.listdir()
# dir1 = os.scandir()
# print(directory)
#
# for dir in dir2:
#     print(dir)

# for dir in directory:
#     print(dir)
#
# for dir in dir1:
#     print(dir)

# basepath = 'venv/'
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath, entry)):
#         print(entry)

os.mkdir("testdir")
print(os.getcwd)


data = 'some data to save'

def read():
    with open('data.txt', 'r') as file:
        print(file.readline(5))
        file.close()


def write():
    with open('data.txt', 'w') as file:
        file.write(data + '\n')
        file.close()


def append():
    with open('data.txt', 'a') as file:
        file.write(data + '\n')
        file.close()


def lineByLine():
    with open('data.txt', 'r')as file:
        line = file.readline()

        while line != '':
            print(line, end='')
            line = file.readline()


def forEachLineByLine():
    with open('data.txt', 'r') as file:
        for line in file.readlines():
            print(line, end='')


forEachLineByLine()
lineByLine()
