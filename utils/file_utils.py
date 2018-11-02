import os

from Colour import Colours, Colour


# Reads the file  of colours
# Returns the number of colours in the file and a list with the colours (RGB) values

def read_file(fname):
    with open(fname, 'r') as afile:
        lines = afile.readlines()
    n = int(lines[3])  # number of colours  in the file
    colours = []
    lines = lines[4:]  # colors as rgb values
    for l in lines:
        colours.append(Colour(l.split()))
    return n, Colours(colours)


def load_file():
    # Get the directory where the file is located
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)  # Change the working directory so we can read the file

    return read_file('../colours.txt')  # Total number of colours and list of colours
