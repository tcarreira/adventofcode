#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))


class Bag:
    def __init__(self, color):
        self.name = color
        self.contains = set()
        self.contained = set()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def append_contains(self, bag):
        self.contains.add(bag)

    def append_contained(self, bag):
        self.contained.add(bag)


seen_bags = {}


def parse_text(text):
    parse1 = text.split(" bags contain ")
    color_from = parse1[0]
    colors_to = []

    part2 = "".join(parse1[1])[:-1]  # remove last dot.

    if part2 != "no other bags":
        parse2 = part2.split(", ")
        for num_color in parse2:
            match = re.search("^([0-9]*) (.*) bags?$", num_color)
            number = match.group(1)
            color = match.group(2)
            colors_to.append(color)

    return color_from, colors_to


def insert_or_get(color):
    if color not in seen_bags:
        bag = Bag(color)
        seen_bags[color] = bag
    return seen_bags[color]


def search_recursive_contained(bag, used_bags=set()):
    if bag in used_bags:
        return 0
    count = 1
    used_bags.add(bag)

    for container_bag in bag.contained:
        count += search_recursive_contained(container_bag, used_bags)

    return count


def main():
    with open(curdir + "/input.txt") as f:

        for line in f.readlines():
            color_from, colors_to = parse_text(line.strip())
            bag_contain = insert_or_get(color_from)

            for color in colors_to:
                bag = insert_or_get(color)
                bag_contain.append_contains(bag)
                bag.append_contained(bag_contain)

    count = search_recursive_contained(seen_bags["shiny gold"]) - 1
    print(f"Result: {count}")


if __name__ == "__main__":
    main()