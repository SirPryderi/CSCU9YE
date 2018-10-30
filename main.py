# Get the directory where the file is located
import os
import random

from Colour import Colour
from algorithms.hillclimbing import hill_climb
from drawColours import read_file, plot_colours, plot_kolours

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)  # Change the working directory so we can read the file

ncolors, colours = read_file('colours.txt')  # Total number of colours and list of colours

test_size = 50  # Size of the subset of colours for testing

# produces random permutation of length test_size, from the numbers 0 to test_size -1

# plot_colours(test_colours, colours, permutation)

random_subset_1 = colours.random_subsets(test_size)

# plot_kolours(random_subset_1)

# random_subset_2 = random_subset_1.copy()
#
# random_subset_2.bubble_swap(0)
#
# plot_kolours(random_subset_2)
#
# print(random_subset_1.is_local_optimum())
# print(random_subset_2.is_local_optimum())


climbed_subset_1 = hill_climb(random_subset_1)

plot_kolours(random_subset_1)
plot_kolours(climbed_subset_1)
