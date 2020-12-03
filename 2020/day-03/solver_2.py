#!/usr/bin/env python3

import os
from solver_1 import build_map, find_collisions

SLOPES = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]


def main():
    map = build_map()

    total = 1
    for slope in SLOPES:
        collisions = find_collisions(map, slope=slope)
        print(f"Collisions found (slope = {slope}): {collisions}")
        total *= collisions

    print("Solution: %s " % total)


if __name__ == "__main__":
    main()