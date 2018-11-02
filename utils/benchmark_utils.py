import time

from Colour import Colours


def benchmark_algorithm(colours_set, algorithm, args=None) -> list:
    if args is None:
        args = []

    for colours in colours_set:
        start_time = time.time()
        algorithm(colours, *args)
        yield time.time() - start_time


def generate_subsets(colours: Colours, count: int, size: int):
    for i in range(count):
        yield colours.random_subsets(size)

# def benchmark_algorithm_scaling(colours, alg)