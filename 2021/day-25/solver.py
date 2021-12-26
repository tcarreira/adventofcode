#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".strip()


def move_cucumbers_east(org_map: list[list[str]]) -> list[list[str]]:
    new_map = [[c for c in line] for line in org_map]
    max_x = len(org_map[0])
    for y, line in enumerate(org_map):
        for x, c in enumerate(line):
            next_x = (x + 1) % max_x
            if c == ">" and org_map[y][next_x] == ".":
                new_map[y][x] = "."
                new_map[y][next_x] = ">"
    return new_map


def move_cucumbers_south(org_map: list[list[str]]) -> list[list[str]]:
    new_map = [[c for c in line] for line in org_map]
    max_y = len(org_map)

    for y, line in enumerate(org_map):
        for x, c in enumerate(line):
            next_y = (y + 1) % max_y
            if c == "v" and org_map[next_y][x] == ".":
                new_map[y][x] = "."
                new_map[next_y][x] = "v"
    return new_map


def part1(p_input):
    step = 0
    cucumber_map = p_input

    while True:
        step += 1
        new_cucumber_map = move_cucumbers_east(cucumber_map)
        new_cucumber_map = move_cucumbers_south(new_cucumber_map)

        if new_cucumber_map == cucumber_map:
            return step
        cucumber_map = new_cucumber_map


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    numbers = [[c for c in line] for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(numbers))


if __name__ == "__main__":
    main()
