import csv
import random

def createFile():
    with open('textFile.txt', 'w') as file:

        for line in range(1000000):
            for line in range(7):
                random_number = str(random.randint(1,100))
                file.write(random_number + '\t')

            file.write(str('\n'))



createFile()


def gamerScoreOpen():
    file = open("gamerscore.csv", "r")  # opens file ready to use
    line = file.readline()  # stores a line in line

    while (line):
        data = line.split(",")  # seperates data into array
        print("Handle: ", data[0])  # printing array at index 0
        print("Gamescore: ", data[1])  # printing array at index 1
        line = file.readline()  # reading next line
    file.close()  # closing file
