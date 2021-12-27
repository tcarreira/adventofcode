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


def part2(p_input):
    # help was needed. A brute force would do it afterall :(
    solution = 0
    for y0 in range(p_input[2] - 1, -p_input[2] + 1):
        for x0 in range(p_input[1] + 1):
            v_x, v_y, x, y = x0, y0, 0, 0
            while True:
                if p_input[0] <= x <= p_input[1] and p_input[2] <= y <= p_input[3]:
                    solution += 1
                    break
                if x > p_input[1] or y < p_input[2]:
                    break

                x, y = x + v_x, y + v_y
                v_x, v_y = max(0, v_x - 1), v_y - 1

    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    xy = re.match(r".*x=([0-9]*)..([0-9]*), y=([-0-9]*)..([-0-9]*)", raw_input).groups()
    borders = (int(xy[0]), int(xy[1]), int(xy[2]), int(xy[3]))

    print("Solution to Part 1:")
    print(part1(borders))

    print("Solution to Part 2:")
    print(part2(borders))


if __name__ == "__main__":
    main()
