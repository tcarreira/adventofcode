#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

curdir = Path(__file__).parent.absolute()


def relax_neighbors(neighbors, active_cubes):
    return set(
        [
            coord
            for coord, val in neighbors.items()
            if val == 3 or (2 == val and coord in active_cubes)
        ]
    )


def set_all_neighbors(cubes, coord):
    for i in range(coord[0] - 1, coord[0] + 2):
        for j in range(coord[1] - 1, coord[1] + 2):
            for k in range(coord[2] - 1, coord[2] + 2):
                for l in range(coord[3] - 1, coord[3] + 2):
                    if (i, j, k, l) != coord:
                        cubes[(i, j, k, l)] += 1


def main(iterations=6):
    active_cubes = set()
    with open(curdir.joinpath("input.txt")) as f:
        for i, line in enumerate(f.readlines()):
            for j, c in enumerate(line.strip()):
                if c == "#":
                    active_cubes.add((i, j, 0, 0))

    for i in range(iterations):
        neighbors = defaultdict(lambda: 0)
        for coord in active_cubes:
            set_all_neighbors(neighbors, coord)

        active_cubes = relax_neighbors(neighbors, active_cubes)

    print(len(active_cubes))


if __name__ == "__main__":
    main()
