#!/usr/bin/env python3
raw_input = open("input.txt").read()
two_parts_input = [part.splitlines() for part in raw_input.split("\n\n")]
dots = set([tuple(map(int, line.split(","))) for line in two_parts_input[0]])
fold_instructions = two_parts_input[1]

for i, fold_instruction in enumerate(fold_instructions):
    x_fold = fold_instruction.split("fold along x=")[-1]
    y_fold = fold_instruction.split("fold along y=")[-1]
    if x_fold.isnumeric():
        x = int(x_fold)
        dots = set([(dot[0] - 2 * max(0, dot[0] - x), dot[1]) for dot in dots])
    if y_fold.isnumeric():
        y = int(y_fold)
        dots = set([(dot[0], dot[1] - 2 * max(0, dot[1] - y)) for dot in dots])

    if i == 0:
        print(f"Solution to part1: {len(dots)}")

print("Solution to part2:")
x_max, y_max = max([c[0] for c in dots]), max([c[1] for c in dots])
for y in range(y_max + 1):
    for x in range(x_max + 1):
        print("█", end="") if (x, y) in dots else print(" ", end="")
    print()
print()
