#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
""".strip()


def printme(coords):
    return
    for y in range(-5, 10):
        for x in range(-5, 10):
            if (x, y) in coords:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def part1(p_input, iterations=2):
    image_enhancement_algorithm = p_input[0]
    raw_map = [line for line in p_input[1].splitlines()]

    # Build a coordinates map
    coordinates = set()
    for y in range(len(raw_map)):
        for x in range(len(raw_map[0])):
            if raw_map[y][x] == "#":
                coordinates.add((x, y))

    for i in range(iterations):
        printme(coordinates)

        new_map = defaultdict(int)
        for x0, y0 in coordinates:
            for x in range(x0 - 3, x0 + 4):
                for y in range(y0 - 3, y0 + 4):
                    new_map[(x, y)] += 1

        if i % 2 == 0:
            min_x = min([x for x, _ in coordinates])
            max_x = max([x for x, _ in coordinates])
            min_y = min([y for _, y in coordinates])
            max_y = max([y for _, y in coordinates])
        else:
            # cleanup infinite borders on odd iterations
            new_map = {
                (x, y): 1
                for x, y in new_map
                if min_x - 2 <= x <= max_x + 2 and min_y - 2 <= y <= max_y + 2
            }

        new_coordinates = set()
        for x0, y0 in new_map:
            hash_str = ""
            for y in range(y0 - 1, y0 + 2):
                for x in range(x0 - 1, x0 + 2):
                    if (x, y) in coordinates:
                        hash_str += "1"
                    else:
                        hash_str += "0"
            idx = int(hash_str, 2)
            if image_enhancement_algorithm[idx] == "#":
                new_coordinates.add((x0, y0))

        coordinates = new_coordinates
    printme(coordinates)

    solution = len(coordinates)
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    raw_input = test_input  # testing with the example - comment for real input
    parts = raw_input.split("\n\n")

    print("Solution to Part 1:")
    print(part1(parts))


if __name__ == "__main__":
    main()
