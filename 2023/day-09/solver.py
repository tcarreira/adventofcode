#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()


def getnext(sequence):
    if not any(sequence):
        return 0

    next = []
    for s1, s2 in zip(sequence, sequence[1:]):
        next.append(s2 - s1)

    return sequence[-1] + getnext(next)


def getprev(sequence):
    if not any(sequence):
        return 0

    next = []
    for s1, s2 in zip(sequence, sequence[1:]):
        next.append(s2 - s1)

    return sequence[0] - getprev(next)


# 0:12:30
def part1(p_input):
    sequences = [[int(i) for i in l.split(" ")] for l in p_input]

    solution = 0
    for s in sequences:
        solution += getnext(s)
    return solution


# 0:21:35
def part2(p_input):
    sequences = [[int(i) for i in l.split(" ")] for l in p_input]

    solution = 0
    for s in sequences:
        solution += getprev(s)
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
