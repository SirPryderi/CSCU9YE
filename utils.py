import os

from drawColours import read_file


def load_file():
    # Get the directory where the file is located
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)  # Change the working directory so we can read the file

    return read_file('colours.txt')  # Total number of colours and list of colours
