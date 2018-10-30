import random

from Colour import Colours


def hill_climb_alt(colours: Colours) -> Colours:
    colours = init(colours)

    while not colours.is_local_optimum():
        colours_prime = colours.copy()
        colours_prime.bubble_swap(random.randint(0, colours_prime.size() - 1))

        if colours_prime.total_distance() < colours.total_distance():
            colours = colours_prime

    return colours


def hill_climb(colours: Colours, iterations) -> Colours:
    colours = init(colours)

    for i in range(iterations):
        colours_prime = colours.copy()

        a = colours.random_index()
        b = colours.random_index()

        colours_prime.invert_region(a, b)

        if colours_prime.total_distance() < colours.total_distance():
            colours = colours_prime

    return colours


def init(colours):
    colours = colours.copy()
    colours.randomise()
    return colours
