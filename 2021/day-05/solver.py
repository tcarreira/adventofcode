#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()


def part1(p_input):
    biggest = max([max([max(pair) for pair in line]) for line in p_input])

    big_map = [[0 for _ in range(biggest + 1)] for _ in range(biggest + 1)]
    for line in p_input:
        a, b = line
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                big_map[a[0]][y] += 1
        elif a[1] == b[1]:
            for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                big_map[x][a[1]] += 1

    solution = 0
    for y in range(biggest + 1):
        for x in range(biggest + 1):
            if big_map[x][y] >= 2:
                solution += 1
        #     print(big_map[x][y] if big_map[x][y] else ".", end="")
        # print()
    return solution


def part2(p_input):
    biggest = max([max([max(pair) for pair in line]) for line in p_input])

    big_map = [[0 for _ in range(biggest + 1)] for _ in range(biggest + 1)]
    for line in p_input:
        a, b = line
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                big_map[a[0]][y] += 1
        elif a[1] == b[1]:
            for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                big_map[x][a[1]] += 1
        else:  # diagonal
            left = min(a, b, key=lambda x: x[0])
            right = a if b == left else b

            y_dir = (right[1] - left[1]) // abs((right[1] - left[1]))  # 1 | -1
            x_range = range(left[0], right[0] + 1)
            y_range = range(left[1], right[1] + y_dir, y_dir)
            for x, y in zip(x_range, y_range):
                big_map[x][y] += 1

    solution = 0
    for y in range(biggest + 1):
        for x in range(biggest + 1):
            if big_map[x][y] >= 2:
                solution += 1
        #     print(big_map[x][y] if big_map[x][y] else ".", end="")
        # print()
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    lines = [
        [[int(c) for c in pairs.split(",")] for pairs in line.split(" -> ")]
        for line in raw_input.splitlines()
    ]

    print("Solution to Part 1:")
    print(part1(lines))

    print("Solution to Part 2:")
    print(part2(lines))


if __name__ == "__main__":
    main()
