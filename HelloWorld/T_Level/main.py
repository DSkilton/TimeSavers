import pyttsx3
from array import *
import math

import tkinter

# help(tkinter)


def load_file_to_list():
    file = open("emotions.txt", "r")
    print(file.read(2))

    print(file.read())



load_file_to_list()

# write a program to find the position of a given number
# in a list of numbers arranged in decreasing order. We #
# also need to minimise the number of time we access elements
# from the list.


#
#
# for i in range(2 ** 2):
#     print('Hello, world!')
#
# dictExample = {"name: Duncan", "age: 35", "education: level 5"}
#
#
# def table():
#     struct = ['question1 ', 'question2 ', 'question3']
#     row1 = ['anwer1', 'answer2', 'answer3']
#     row2 = ['answer1', 'answer2', 'answer3']
#     row3 = ['answer1', 'answer2', 'answer3']
#
#     titles = ['struc', 'array1', 'tuple1', 'list1']
#     data = [titles] + list(zip(struct, row1, row2, row3))
#
#     for i, d in enumerate(data):
#         line = '|'.join(str(x).ljust(12) for x in d)
#         print(line)
#         if i == 0:
#             print('-' * len(line))
#
#
# table()
#
# def list():
#     list = [1, "I" , 3, "love", 5, "programming"]
#     print(list.reverse())
#     print(list[1])
#     print(list[3])
#     print(list[5])
#     listId = id(list)
#     listIdHex = hex(listId)
#
#     print("Location in memory " + str(listId))
#     print("Hex location " + str(listIdHex))
#
#
# array_num = array('i', [1, 3, 5, 7, 9])
# print("Original array: "+str(array_num))
# print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
# print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))
#
# def chat():
#     engine = pyttsx3.init()
#     engine.say("All the chat")
#     engine.runAndWait()
#
# def fizzBuzz():
#     for i in range (1, 50):
#         if i % 3 == 0 and i % 5 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)
#
