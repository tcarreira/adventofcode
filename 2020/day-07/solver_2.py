#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))


class Bag:
    def __init__(self, color):
        self.name = color
        self.contains = {}
        self.contained = set()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def append_contains(self, bag, count):
        self.contains[bag] = count

    def append_contained(self, bag):
        self.contained.add(bag)


seen_bags = {}


def parse_text(text):
    parse1 = text.split(" bags contain ")
    color_from = parse1[0]
    colors_to = {}

    part2 = "".join(parse1[1])[:-1]  # remove last dot.

    if part2 != "no other bags":
        parse2 = part2.split(", ")
        for num_color in parse2:
            match = re.search("^([0-9]*) (.*) bags?$", num_color)
            number = int(match.group(1))
            color = match.group(2)
            colors_to[color] = number

    return color_from, colors_to


def insert_or_get(color):
    if color not in seen_bags:
        bag = Bag(color)
        seen_bags[color] = bag
    return seen_bags[color]


def count_how_many_bags(bag):
    count = 0
    for inner_bag, inner_count in bag.contains.items():
        inside_count = count_how_many_bags(inner_bag)
        count += inner_count + inner_count * inside_count

    return count


def main():
    with open(curdir + "/input.txt") as f:

        for line in f.readlines():
            color_from, colors_to = parse_text(line.strip())
            bag_contain = insert_or_get(color_from)

            for color, number in colors_to.items():
                bag = insert_or_get(color)
                bag_contain.append_contains(bag, number)
                bag.append_contained(bag_contain)

    count = count_how_many_bags(seen_bags["shiny gold"])
    print(f"Result: {count}")


if __name__ == "__main__":
    main()