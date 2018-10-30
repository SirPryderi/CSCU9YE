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
        return self.random_subsets(self.size())

    def random_subsets(self, size):
        return Colours(random.sample(self.list, size))

    def total_distance(self) -> float:
        distance = 0

        for i in range(self.size() - 1):
            distance += self.at(i).distance(self.at(i + 1))

        return distance

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
