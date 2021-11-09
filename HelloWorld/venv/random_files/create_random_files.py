import os
from pathlib import Path
import random


list_of_extensions = ['.rst','.txt','.md','.docx','.odt','.html','.ppt','.doc']


# get into the RandomFiles directory
os.chdir('./RandomFiles')

for item in list_of_extensions:
    # create 20 random files for each file extension
    for num in range(20):
        # let the file begin with a random number between 1 to 50
        file_name = random.randint(1,50)
        file_to_create = str(file_name) + item
        Path(file_to_create).touch()