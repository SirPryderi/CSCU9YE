from algorithms.greedyconstructive import greedy_constructive
from algorithms.hillclimbing import hill_climb
from algorithms.multi_hc import multi_hc
from algorithms.spectrum import spectrum_sort_shake, spectrum_sort
from utils.draw_utils import plot_kolours
from utils.file_utils import load_file

size, colours = load_file()

# Options

test_size = 100  # Size of the subset of colours for testing
iterations = 1000  # Maximum number of iterations
mhc_runs = 50  # Number of runs for the MHC

random_subset_1 = colours.random_subsets(test_size)

# Algorithm Runs

constructive_subset_1 = greedy_constructive(random_subset_1)
hill_climb_subset_1 = hill_climb(random_subset_1, iterations)

multi_hc_subset_1, _ = multi_hc(random_subset_1, iterations, mhc_runs)
spectrum_subset_2 = spectrum_sort(random_subset_1)
spectrum_subset_1 = spectrum_sort_shake(random_subset_1)

# Plotting

plot_kolours(random_subset_1, "Original Set")
plot_kolours(constructive_subset_1, "Constructive Heuristics")
plot_kolours(hill_climb_subset_1, "Hill Climbing")
plot_kolours(multi_hc_subset_1, "Multi Hill Climbing")
plot_kolours(spectrum_subset_2, "Spectrum Sorting v1")
plot_kolours(spectrum_subset_1, "Spectrum Sorting v2")
