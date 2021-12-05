#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
1
2
3
""".strip()


def part1(p_input):
    solution = p_input
    return solution


def part2(p_input):
    solution = p_input
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    raw_input = test_input  # testing with the example - comment for real input
    numbers = [int(line) for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(numbers))

    # print("Solution to Part 2:")
    # print(part2(numbers))


if __name__ == "__main__":
    main()
