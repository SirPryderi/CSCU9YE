import random

from Colour import Colours


def hill_climb(colours: Colours) -> Colours:
    colours = colours.copy()
    colours.randomise()

    while not colours.is_local_optimum():
        colours_prime = colours.copy()
        colours_prime.bubble_swap(random.randint(0, colours_prime.size() - 1))

        if colours_prime.total_distance() < colours.total_distance():
            colours = colours_prime

    return colours
