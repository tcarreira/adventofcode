#!/usr/bin/env python3

import re
from collections import defaultdict
from pathlib import Path

curdir = Path(__file__).parent.absolute()


def sum_coords(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1], coord1[2] + coord2[2])


def main():
    with open(curdir.joinpath("input.txt")) as f:
        tile_coords = f.read().splitlines()

    black_tiles = set()

    for tile in tile_coords:
        i = 0
        position = (0, 0, 0)
        while i < len(tile.strip()):
            if i < len(tile.strip()) - 1 and tile[i : i + 2] == "se":
                position = (
                    position[0] + 1,
                    position[1],
                    position[2] - 1,
                )
                i += 2
            elif i < len(tile.strip()) - 1 and tile[i : i + 2] == "sw":
                position = (
                    position[0],
                    position[1] - 1,
                    position[2] - 1,
                )
                i += 2
            elif i < len(tile.strip()) - 1 and tile[i : i + 2] == "ne":
                position = (
                    position[0],
                    position[1] + 1,
                    position[2] + 1,
                )
                i += 2
            elif i < len(tile.strip()) - 1 and tile[i : i + 2] == "nw":
                position = (
                    position[0] - 1,
                    position[1],
                    position[2] + 1,
                )
                i += 2
            elif tile[i] == "e":
                position = (
                    position[0] + 1,
                    position[1] + 1,
                    position[2],
                )
                i += 1
            elif tile[i] == "w":
                position = (
                    position[0] - 1,
                    position[1] - 1,
                    position[2],
                )
                i += 1
            else:
                print(f"Fuuuuuu. i={i}, line={tile}")
                return

        print(position)
        if position in black_tiles:
            black_tiles.remove(position)
        else:
            black_tiles.add(position)

    print("Solution1: ", len(black_tiles))

    for day in range(100):
        neighbors = defaultdict(lambda: 0)
        for tile in black_tiles:
            for neigh in [
                (1, 1, 0),
                (0, 1, 1),
                (-1, 0, 1),
                (-1, -1, 0),
                (0, -1, -1),
                (1, 0, -1),
            ]:
                neighbors[sum_coords(tile, neigh)] += 1

        next_black_tiles = set()
        for coord in black_tiles:
            if coord in neighbors and 0 < neighbors[coord] <= 2:
                next_black_tiles.add(coord)

        for coord, neighs in neighbors.items():
            if neighs == 2:
                next_black_tiles.add(coord)

        # print(f"Day {day+1} : ", len(next_black_tiles))
        black_tiles = next_black_tiles

    print("Solution2: ", len(black_tiles))


if __name__ == "__main__":
    main()
