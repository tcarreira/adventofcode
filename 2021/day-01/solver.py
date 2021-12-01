#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
199
200
208
210
200
207
240
269
260
263
""".strip()

def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example
    numbers = list(map(int, raw_input.splitlines()))

    print("Solution to Part 1:")
    print(part1(numbers))

    print("Solution to Part 2:")
    print(part2(numbers))


def part1(p_input):
    counter = 0
    for i in range(1,len(p_input)):
        if p_input[i] > p_input[i-1]:
            counter += 1
    return counter

def part2(p_input):
    sliding = [ sum(p_input[i-3:i]) for i in range(3,len(p_input)+1) ]
    return part1(sliding)


if __name__ == "__main__":
    main()
