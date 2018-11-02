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


def benchmark_boxplot(times, labels=None):
    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))
    # Create an axes instance
    ax = fig.add_subplot(111)
    # Create the boxplot
    bp = ax.boxplot(times, labels=labels)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
    ax.set_ylabel('Execution time ($s$)')
    ax.set_title('Algorithms execution time for %d iterations' % len(times[0]))
    # Save the figure
    fig.savefig('../imgs/benchmark_boxplot.png', bbox_inches='tight')
    plt.show()


def unpack(algorithms: list) -> (list, list, list):
    labels = [row[0] for row in algorithms]
    functions = [row[1] for row in algorithms]
    args = [row[2] for row in algorithms]

    return labels, functions, args


def benchmark_barchart_error(algorithms, times):
    labels, functions, args = unpack(algorithms)

    arrays = []
    means = []
    stds = []

    for arr in times:
        arrays.append(np.array(arr))

    for array in arrays:
        means.append(np.mean(array))
        stds.append(np.std(array))

    x_pos = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.bar(x_pos, means, yerr=stds, align='center', alpha=0.5, ecolor='black', capsize=10)

    ax.set_ylabel('Average execution time ($s$)')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_title('Algorithms execution time for %d iterations' % len(times[0]))
    ax.yaxis.grid(True)

    # Save the figure and show
    plt.tight_layout()
    plt.savefig('../imgs/benchmark_barchart.png')
    plt.show()
