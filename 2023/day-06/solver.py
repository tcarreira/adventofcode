#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
Time:      7  15   30
Distance:  9  40  200
""".strip()

# 0:07:12
def part1(p_input):
    times = [int(l) for l in p_input[0].split(":")[1].split(" ") if l != ""]
    dists = [int(l) for l in p_input[1].split(":")[1].split(" ") if l != ""]

    solution = 1
    for mt, md in zip(times, dists):
        ways = 0
        for t in range(mt + 1):
            d = (mt - t) * t
            if d > md:
                ways += 1
        solution *= ways
    return solution

# 0:09:19
def part2(p_input):
    time = int("".join([l for l in p_input[0].split(":")[1].split(" ") if l != ""]))
    dist = int("".join([l for l in p_input[1].split(":")[1].split(" ") if l != ""]))

    solution = 0
    for t in range(time + 1):
        d = (time - t) * t
        if d > dist:
            solution += 1
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input

    # simple treat input
    p_input = [line for line in raw_input.splitlines()]
    # p_input = [int(line) for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(p_input))

    print("Solution to Part 2:")
    print(part2(p_input))


if __name__ == "__main__":
    main()
