from Colour import Colours


def spectrum_sort(colours: Colours) -> Colours:
    return Colours(sorted(colours.list, key=lambda colour: colour.hue))


def spectrum_sort_shake(colours: Colours) -> Colours:
    spectrum_colours = spectrum_sort(colours)

    cocktail_shaker_sort(spectrum_colours)

    return spectrum_colours


def cocktail_shaker_sort(colours: Colours) -> Colours:
    # a sorting algorithm similar to the cocktail shaker sort
    # https://en.wikipedia.org/wiki/Cocktail_shaker_sort

    changed = True

    while changed:
        changed = False

        def shake(it):
            global changed
            t = colours.total_distance()
            colours.bubble_swap(it)

            if colours.total_distance() >= t:
                colours.bubble_swap(it)
            else:
                changed = True

        # bubble sort left to right
        for i in range(colours.size()):
            shake(i)

        # bubble sort right to left
        for i in range(colours.size(), 0):
            shake(i)

    return colours
