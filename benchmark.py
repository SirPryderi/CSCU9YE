from algorithms.greedyconstructive import greedy_constructive
from algorithms.hillclimbing import hill_climb
from algorithms.multi_hc import multi_hc
from algorithms.spectrum import spectrum_sort_shake
from utils.benchmark_utils import generate_subsets, benchmark_algorithm_scaling, benchmark_algorithm
from utils.draw_utils import benchmark_boxplot, benchmark_barchart_error, benchmark_plot_algorithm
from utils.file_utils import load_file

number_of_subsets = 20
size_of_subsets = 200

max_iterations = 100
hc_count = 20

algorithms = [
    ["Constructive", greedy_constructive, None, 'red'],
    ["Hill Climb (%d iter.)" % max_iterations, hill_climb, [max_iterations], 'green'],
    ["MHC (%d iter. %d runs)" % (max_iterations, hc_count), multi_hc, [max_iterations, hc_count], 'blue'],
    ["Spectrum", spectrum_sort_shake, None, 'purple']
]

size, colours = load_file()

# subsets = list(generate_subsets(colours, number_of_subsets, size_of_subsets))
#
# times = []
# for algorithm in algorithms:
#     times.append(list(benchmark_algorithm(subsets, algorithm[1], algorithm[2])))
#
# benchmark_boxplot(times, [row[0] for row in algorithms])
#
# benchmark_barchart_error(algorithms, times)
#
result = benchmark_algorithm_scaling(colours, algorithms, 100, 5)

benchmark_plot_algorithm(algorithms, result, [2])
