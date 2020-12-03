#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))
TREE = "#"


def build_map():
    map = []
    with open(curdir + "/input.txt") as f:
        for line in f.readlines():
            map.append(line.strip())
    return map


def advance(position, slope):
    return (
        position[0] + slope[0],
        position[1] + slope[1],
    )


def find_collisions(map, slope=(1, 3)):
    position = (0, 0)
    collisions = 0
    wide = len(map[0])

    while position[0] < len(map):
        y = position[0]
        x = position[1] % wide

        if map[y][x] == TREE:
            collisions += 1
        position = advance(position, slope)

    return collisions


def main():
    map = build_map()
    print("Collisions found: %s " % find_collisions(map))


if __name__ == "__main__":
    main()