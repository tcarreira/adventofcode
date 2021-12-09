#!/usr/bin/env python3

from pathlib import Path
from collections import Counter

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


def part1(p_input):
    solution = 0

    y_max = len(p_input) - 1
    x_max = len(p_input[0]) - 1
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if y > 0 and p_input[y - 1][x] <= p_input[y][x]:
                continue
            if x > 0 and p_input[y][x - 1] <= p_input[y][x]:
                continue
            if y < y_max and p_input[y + 1][x] <= p_input[y][x]:
                continue
            if x < x_max and p_input[y][x + 1] <= p_input[y][x]:
                continue
            # print(f"Found a minimum at ({x},{y}) with value {p_input[y][x]}")
            solution += 1 + p_input[y][x]

    return solution


def part2(p_input):
    def get_low_points():
        # part 1 code, with low_points variable
        low_points = []
        y_max = len(p_input) - 1
        x_max = len(p_input[0]) - 1
        for y in range(y_max + 1):
            for x in range(x_max + 1):
                if y > 0 and p_input[y - 1][x] <= p_input[y][x]:
                    continue
                if x > 0 and p_input[y][x - 1] <= p_input[y][x]:
                    continue
                if y < y_max and p_input[y + 1][x] <= p_input[y][x]:
                    continue
                if x < x_max and p_input[y][x + 1] <= p_input[y][x]:
                    continue
                low_points.append((x, y))
        return low_points

    basin_map = [[0] * len(p_input[0]) for _ in p_input]
    basin_count = Counter()

    def traverse(index, x, y):
        if x < 0 or y < 0 or x >= len(p_input[0]) or y >= len(p_input):
            return  # out of bounds

        if basin_map[y][x] == 0 and p_input[y][x] < 9:
            basin_map[y][x] = index
            basin_count[index] += 1
            traverse(index, x - 1, y)  # left
            traverse(index, x, y - 1)  # up
            traverse(index, x + 1, y)  # right
            traverse(index, x, y + 1)  # down

    for i, point in enumerate(get_low_points()):
        traverse(i + 1, *point)

    mcb = basin_count.most_common()[:3]
    solution = mcb[0][1] * mcb[1][1] * mcb[2][1]
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    numbers = [[int(p) for p in line] for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(numbers))

    print("Solution to Part 2:")
    print(part2(numbers))


if __name__ == "__main__":
    main()
