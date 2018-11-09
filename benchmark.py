import numpy as np

from algorithms.greedyconstructive import greedy_constructive
from algorithms.hillclimbing import hill_climb
from algorithms.multi_hc import multi_hc
from algorithms.spectrum import spectrum_sort_shake
from utils.benchmark_utils import generate_subsets, benchmark_algorithm, benchmark_algorithm_scaling
from utils.draw_utils import plot_progress, plot_hc_results, benchmark_boxplot, benchmark_barchart_error, \
    benchmark_plot_algorithm
from utils.file_utils import load_file

number_of_subsets = 20
size_of_subsets = 500

max_iterations = 100  # optimal value: 5000 - but extremely slow. Keep it to 100 for faster results
hc_count = 30

algorithms = [
    ["Constructive", greedy_constructive, None, 'red'],
    ["Hill Climb (%d iter.)" % max_iterations, hill_climb, [max_iterations], 'green'],
    ["MHC (%d iter. %d runs)" % (max_iterations, hc_count), multi_hc, [max_iterations, hc_count], 'blue'],
    # ["Spectrum v1", spectrum_sort, None, 'violet'],
    ["Spectrum v2", spectrum_sort_shake, None, 'purple']
]

size, colours = load_file()

subsets = list(generate_subsets(colours, number_of_subsets, size_of_subsets))

times = []
for algorithm in algorithms:
    algorithm_times = list(benchmark_algorithm(subsets, algorithm[1], algorithm[2]))
    times.append(algorithm_times)
    print("%s min/avg/max/std = %.2f/%.2f/%.2f/%.2f ms" % (
        algorithm[0],
        np.min(algorithm_times) * 1000,
        np.average(algorithm_times) * 1000,
        np.max(algorithm_times) * 1000,
        np.std(algorithm_times) * 1000,
    ))

benchmark_boxplot(times, [row[0] for row in algorithms])

benchmark_barchart_error(algorithms, times)

result = benchmark_algorithm_scaling(colours, algorithms, size_of_subsets, 5)

benchmark_plot_algorithm(algorithms, result, [])
benchmark_plot_algorithm(algorithms, result, [2])

progress = []

hill_climb(subsets[0], max_iterations, progress)
_, results = multi_hc(subsets[0], max_iterations, hc_count)

plot_progress(progress, "Change of value during Hill Climbing (%d colours)" % size_of_subsets)
plot_hc_results(results, 'Objective values (%d starts, %d colours)' % (len(results), size_of_subsets))
