import math

from Colour import Colours


def lowest_num(colour, colours_list):
    current_lowest = math.inf
    lowest_index = -1

    for i in range(0, colours_list.size()):
        curr_colour = colours_list.at(i)
        current_distance = colour.distance(curr_colour)

        if current_distance < current_lowest:
            current_lowest = current_distance
            lowest_index = i

    return lowest_index


def greedy_constructive(colours: Colours):
    colours = colours.copy()
    sorted_colours = Colours([])

    randint = colours.random_index()

    start_color = colours.remove_index(randint)
    sorted_colours.list.append(start_color)

    while colours.size() > 0:
        closest = lowest_num(start_color, colours)
        new_colour = colours.remove_index(closest)
        sorted_colours.list.append(new_colour)
        start_color = new_colour

    return sorted_colours
