#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip()


def part1():
    # I made it by hand :p
    solution = sum(
        [
            2000,
            3,
            3000,
            6,
            5000,
            20,
            600,
            30,
            600,
            50,
            3,
            8,
        ]
    )
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    raw_input = test_input  # testing with the example - comment for real input

    print("Solution to Part 1:")
    print(part1())



if __name__ == "__main__":
    main()
