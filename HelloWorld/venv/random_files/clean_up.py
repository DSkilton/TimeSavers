import os
import shutil
import glob

# get into the RandomFiles directory
os.chdir('./RandomFiles')

# get the list of files in the directory RandomFiles
files_to_group = []
for random_file in os.listdir('.'):
    print(random_file)
    files_to_group.append(random_file)

# get all the file extensions present
file_extensions = []
for our_file in files_to_group:
    file_extensions.append(os.path.splitext(our_file)[1])#the number 1 is an index number

print(set(file_extensions))

file_types = set(file_extensions) # what is a set data structure and why do you think

for type in file_types:
    new_directory = type.replace(".", " ")
    os.mkdir(new_directory)  # create directory with given name

    for fname in glob.glob(f'*.{type[1:]}'):
        shutil.move(fname, new_directory)
