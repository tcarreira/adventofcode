#!/usr/bin/env python3

from pathlib import Path
from collections import Counter

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = "3,4,3,1,2"


def part1(p_input, days=80):
    counter = Counter(p_input)

    for _ in range(days):
        tmp_counter = Counter()
        for timer, amount in counter.items():
            if timer == 0:
                tmp_counter[6] += amount
                tmp_counter[8] += amount
            else:
                tmp_counter[timer - 1] += amount
        counter = tmp_counter

    return sum(counter.values())


def part2(p_input):
    return part1(p_input, 256)


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    initial_state = [int(number) for number in raw_input.split(",")]

    print("Solution to Part 1:")
    print(part1(initial_state))

    print("Solution to Part 2:")
    print(part2(initial_state))


def minimal(my_input_str):
    fish_counter = Counter(map(int, my_input_str.split(",")))
    for day in range(256):
        if day == 80:
            print("Solution to part 1:", sum(fish_counter.values()))

        tmp_counter = Counter()
        for timer, amount in fish_counter.items():
            if timer == 0:
                tmp_counter[6] += amount
                tmp_counter[8] += amount
            else:
                tmp_counter[timer - 1] += amount
        fish_counter = tmp_counter
    print("Solution to part 2:", sum(fish_counter.values()))


if __name__ == "__main__":
    main()
    minimal(test_input)
