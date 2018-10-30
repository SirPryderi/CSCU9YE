from algorithms.hillclimbing import hill_climb
from algorithms.greedyconstructive import greedy_constructive

from drawColours import plot_kolours
from utils import load_file

size, colours = load_file()

test_size = 50  # Size of the subset of colours for testing

random_subset_1 = colours.random_subsets(test_size)

climbed_subset_1 = hill_climb(random_subset_1)
greedy_subset_1 = greedy_constructive(climbed_subset_1)

plot_kolours(random_subset_1)
plot_kolours(climbed_subset_1)
plot_kolours(greedy_subset_1)
