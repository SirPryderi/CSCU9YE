import colorsys
import math
import random


class Colour:
    def __init__(self, rgb):
        self.r = float(rgb[0])
        self.g = float(rgb[1])
        self.b = float(rgb[2])

    def distance(self, color) -> float:
        return math.sqrt(
            (self.r - color.r) ** 2 +
            (self.g - color.g) ** 2 +
            (self.b - color.b) ** 2
        )

    def to_array(self) -> list:
        return [self.r, self.g, self.b]

    def to_hsv(self) -> list:
        return colorsys.rgb_to_hsv(self.r, self.g, self.b)

    @property
    def hue(self) -> float:
        return self.to_hsv()[0]


class Colours:
    def __init__(self, colour_list: list):
        self.list = colour_list

    def size(self) -> int:
        return len(self.list)

    def at(self, i: int) -> Colour:
        return self.list[i]

    def copy(self):
        return Colours(self.list.copy())

    def randomise(self):
        return random.shuffle(self.list)

    def random_subsets(self, size):
        return Colours(random.sample(self.list, size))

    def total_distance(self) -> float:
        distance = 0

        for i in range(self.size() - 1):
            distance += self.at(i).distance(self.at(i + 1))

        return distance

    def random_index(self) -> int:
        if self.size() > 0:
            return random.randint(0, self.size() - 1)
        else:
            return 0

    def remove_index(self, i) -> Colour:
        return self.list.pop(i)

    def invert_region(self, a, b):
        if a > b:
            temp = a
            a = b
            b = temp

        stop = (b - a) // 2

        for i in range(0, stop):
            self.swap(a + i, b - i)

    def is_local_optimum(self) -> bool:
        total_distance = self.total_distance()

        for i in range(self.size()):
            permutation = self.copy()
            permutation.bubble_swap(i)

            if permutation.total_distance() < total_distance:
                return False

        return True

    def swap(self, a, b):
        """Swaps color at index a with colour at index """

        assert 0 <= a < self.size()
        assert 0 <= b < self.size()

        temp = self.list[a]
        self.list[a] = self.list[b]
        self.list[b] = temp

    def bubble_swap(self, i):
        """Swaps colour at index i with colour at i + 1"""
        size = self.size()

        if i == size - 1:
            next_i = 0
        else:
            next_i = i + 1

        self.swap(i, next_i)
