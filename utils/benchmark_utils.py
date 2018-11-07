import time

from Colour import Colours


def benchmark_algorithm(colours_set, algorithm, args=None):
    if args is None:
        args = []

    for colours in colours_set:
        start_time = time.time()
        algorithm(colours, *args)
        yield time.time() - start_time


def generate_subsets(colours: Colours, count: int, size: int):
    for i in range(count):
        yield colours.random_subsets(size)


def benchmark_algorithm_scaling(colours, algorithms, max_size, step):
    results = []

    for _ in algorithms:
        results.append([[], []])

    for size in range(1, max_size + 1, step):
        subset = colours.random_subsets(size)

        for index, algorithm in enumerate(algorithms):
            execution_time = benchmark_algorithm([subset, ], algorithm[1], algorithm[2]).__next__()
            results[index][0].append(size)
            results[index][1].append(execution_time)

    return results
