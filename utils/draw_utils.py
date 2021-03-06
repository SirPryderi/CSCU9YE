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
    plt.text(0, 25, 'Total distance (value): %d' % colours.total_distance())
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


def plot_line(result, algorithms, index):
    plt.plot(*result[index], color=algorithms[index][3], label=algorithms[index][0])


def benchmark_plot_algorithm(algorithms, result, excluded=[]):
    plt.figure()

    for index, _ in enumerate(algorithms):
        if index in excluded: continue
        plot_line(result, algorithms, index)

    plt.legend()
    plt.title("Execution time over size of dataset")
    plt.xlabel("Number of colours")
    plt.ylabel("Execution time ($s$)")
    plt.savefig('../imgs/benchmark_compare_scaling.png')
    plt.show()


def plot_progress(progress, title):
    plt.figure()
    plt.plot(progress)
    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel("Value (total distance)")
    plt.show()


def plot_hc_results(results, title):
    values = []

    for result in results:
        values.append(result.total_distance())

    # mean
    # median
    # standard deviation

    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))
    # Create an axes instance
    ax = fig.add_subplot(111)
    plot_stats(values, ax)
    # Create the boxplot
    ax.boxplot(values, showmeans=True)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
    ax.set_ylabel('Total distance')
    ax.set_title(title)
    # Save the figure
    fig.savefig('../imgs/benchmark_hc_results.png', bbox_inches='tight')
    plt.show()


def plot_stats(values, ax):
    sigma = np.std(values)
    median = np.median(values)
    mu = np.mean(values)

    textstr = '\n'.join((
        r'$\mu=%.2f$' % (mu,),
        r'$\mathrm{median}=%.2f$' % (median,),
        r'$\sigma=%.2f$' % (sigma,)))

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
