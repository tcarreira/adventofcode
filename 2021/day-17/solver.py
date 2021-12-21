#!/usr/bin/env python3

from pathlib import Path
import re

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = "target area: x=20..30, y=-10..-5"


def part1(p_input):
    y = -min(p_input[2:]) - 1
    solution = y * (y + 1) // 2
    return solution

def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    raw_input = test_input  # testing with the example - comment for real input
    xy = re.match(r".*x=([0-9]*)..([0-9]*), y=([-0-9]*)..([-0-9]*)", raw_input).groups()
    borders = (int(xy[0]), int(xy[1]), int(xy[2]), int(xy[3]))

    print("Solution to Part 1:")
    print(part1(borders))


if __name__ == "__main__":
    main()
