file = open("gamerscore.csv", "r")
line = file.readline()

while(line):
    print(line)
    line=file.readline()

file.close()