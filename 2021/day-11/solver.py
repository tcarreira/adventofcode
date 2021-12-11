#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()


def print_octos(octopusses):
    for l in octopusses:
        print("".join([str(o) if o > 0 else "●" for o in l]))


def iterate(octopusses, flashed=set()):
    # increase energy level by flashed octopus
    for x, y in flashed:
        for y1 in range(max(0, y - 1), min(len(octopusses) - 1, y + 1) + 1):
            for x1 in range(max(0, x - 1), min(len(octopusses[0]) - 1, x + 1) + 1):
                if octopusses[y1][x1] != 0:
                    octopusses[y1][x1] += 1

    count = 0
    flashing = set()
    # find flashing octopus
    for y, l in enumerate(octopusses):
        for x, o in enumerate(l):
            if o > 9:
                octopusses[y][x] = 0
                count += 1
                flashing.add((x, y))

    # iterate if any new flashing octopus
    if count == 0:
        return 0
    return count + iterate(octopusses, flashed=flashing)


def part1(p_input, steps=100, is_part_2=False):
    octopusses = [[o for o in line] for line in p_input]
    solution = 0
    for step in range(steps):
        if is_part_2 and sum([sum(line) for line in octopusses]) == 0:
            return step

        # increase energy level by new step:
        next = [[o + 1 for o in line] for line in octopusses]
        # increase energy level by flashing octopus:
        solution += iterate(next)

        octopusses = [[o if o <= 9 else 0 for o in line] for line in next]
    return solution


def part2(p_input):
    return part1(p_input, steps=100000, is_part_2=True)


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    octos = [[int(octo) for octo in line] for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(octos))

    print("Solution to Part 2:")
    print(part2(octos))


if __name__ == "__main__":
    main()
