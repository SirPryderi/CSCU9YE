from algorithms.greedyconstructive import greedy_constructive
from algorithms.hillclimbing import hill_climb
from drawColours import plot_kolours
from utils import load_file

size, colours = load_file()

# Options

test_size = 10  # Size of the subset of colours for testing
max_iterations = 2000  # Maximum number of iterations

random_subset_1 = colours.random_subsets(test_size)

# Algorithm Runs

hill_climb_subset_1 = hill_climb(random_subset_1, max_iterations)
# multi_hc_subset_1 = multi_hc(random_subset_1, max_iterations, 30)
constructive_subset_1 = greedy_constructive(hill_climb_subset_1)

# Plotting

plot_kolours(random_subset_1, "Original Set")
plot_kolours(hill_climb_subset_1, "Hill Climbing")
# plot_kolours(multi_hc_subset_1, "Multi Hill Climbing")
plot_kolours(constructive_subset_1, "Constructive Heuristics")
