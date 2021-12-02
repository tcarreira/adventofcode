#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    instructions = [
        (instr, int(amount))
        for (instr, amount) in [line.split(" ") for line in raw_input.splitlines()]
    ]

    print("Solution to Part 1:")
    print(part1(instructions))

    print("Solution to Part 2:")
    print(part2(instructions))


def part1(p_input):
    horizontal = depth = 0
    for command, value in p_input:
        if command == "forward":
            horizontal += value
        if command == "up":
            depth -= value
        if command == "down":
            depth += value

    print(f"horizontal={horizontal}, depth={depth}")
    solution = horizontal * depth
    return solution


def part2(p_input):
    horizontal = depth = aim = 0
    for command, value in p_input:
        if command == "forward":
            horizontal += value
            depth += aim * value
        if command == "up":
            aim -= value
        if command == "down":
            aim += value

    print(f"horizontal={horizontal}, depth={depth}")
    solution = horizontal * depth
    return solution


if __name__ == "__main__":
    main()
