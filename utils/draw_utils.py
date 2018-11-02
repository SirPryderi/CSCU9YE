import matplotlib.pyplot as plt
import numpy as np

from Colour import Colour, Colours


# Display the colours in the order of the permutation in a pyplot window
# Input, list of colours, and ordering  of colours.
# They need to be of the same length


def plot_colours(col, colours, perm):
    assert len(col) == len(perm)

    ratio = 10  # ratio of line height/width, e.g. colour lines will have height 10 and width 1
    img = np.zeros((ratio, len(col), 3))

    for i in range(0, len(col)):
        img[:, i, :] = colours[perm[i]].to_array()

    fig, axes = plt.subplots(1, figsize=(8, 4))  # figsize=(width,height) handles window dimensions
    axes.imshow(img, interpolation='nearest')
    axes.axis('off')
    plt.show()


def plot_kolours(colours: Colours, title):
    ratio = 10
    img = np.zeros((ratio, len(colours.list), 3))

    for index, color in enumerate(colours.list):  # type: (int, Colour)
        img[:, index, :] = color.to_array()

    fig, axes = plt.subplots(1, figsize=(8, 4))  # figsize=(width,height) handles window dimensions
    axes.imshow(img, interpolation='nearest')
    axes.axis('off')
    axes.set_title(title)
    plt.show()
