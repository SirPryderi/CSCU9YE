import math

from Colour import Colours
from algorithms.hillclimbing import hill_climb


def multi_hc(colours: Colours, iterations, count) -> (Colours, list):
    solutions = []
    best_solution = None
    best_distance = math.inf

    # return all results for comparison

    for i in range(count):
        new_solution = hill_climb(colours, iterations)
        new_distance = new_solution.total_distance()

        if new_distance < best_distance:
            best_distance = new_distance
            best_solution = new_solution

        solutions.append(new_solution)

    return best_solution, solutions
