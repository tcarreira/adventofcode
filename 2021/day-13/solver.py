#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip()


def print_dots(coords):
    x_max = max([c[0] for c in coords])
    y_max = max([c[1] for c in coords])
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if (x, y) in coords:
                print("██", end="")
            else:
                print("  ", end="")
        print()
    print()


def part1(dots, instructions, many_folds=1):
    for instruction in instructions[0:many_folds]:
        x_fold = instruction.split("fold along x=")[-1]
        y_fold = instruction.split("fold along y=")[-1]
        if x_fold.isnumeric():
            x = int(x_fold)
            dots = set([(dot[0] - 2 * max(0, dot[0] - x), dot[1]) for dot in dots])
        if y_fold.isnumeric():
            y = int(y_fold)
            dots = set([(dot[0], dot[1] - 2 * max(0, dot[1] - y)) for dot in dots])

    # part 2
    if many_folds is None:
        return dots

    return len(dots)


def part2(dots, instructions):
    solution = part1(dots, instructions, None)
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    p_input = [part.splitlines() for part in raw_input.split("\n\n")]
    dots = [tuple(map(int, line.split(","))) for line in p_input[0]]
    instructions = p_input[1]
    print("Solution to Part 1:")
    print(part1(dots, instructions))

    print("Solution to Part 2:")
    print_dots(part2(dots, instructions))


if __name__ == "__main__":
    main()
