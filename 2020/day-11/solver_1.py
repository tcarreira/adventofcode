#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))

C = {
    "empty": "L",
    "occupied": "#",
    "floor": ".",
}


def get_new_cell(seats_map, row, col):
    if seats_map[row][col] == C["floor"]:
        return C["floor"]

    count = 0
    for i in range(max(0, row - 1), 1 + min(row + 1, len(seats_map) - 1)):
        for j in range(max(0, col - 1), 1 + min(col + 1, len(seats_map[0]) - 1)):
            if seats_map[i][j] == C["occupied"] and (i, j) != (row, col):
                count += 1

    if seats_map[row][col] == C["empty"] and count == 0:
        return C["occupied"]
    if seats_map[row][col] == C["occupied"] and count >= 4:
        return C["empty"]
    return seats_map[row][col]


def map_iteration(seats_map):
    new_map = []
    changes = 0
    for i, line in enumerate(seats_map):
        new_map.append("")
        for j, cell in enumerate(line):
            new_cell = get_new_cell(seats_map, i, j)
            new_map[i] += new_cell
            if new_cell != cell:
                changes += 1

    return new_map, changes


def main():
    seats_map = []
    with open(curdir + "/input.txt") as f:
        for line in f.readlines():
            seats_map.append(line.strip())

    iterations = 0
    changes = 1
    while changes > 0:
        iterations += 1
        seats_map, changes = map_iteration(seats_map)

    count = 0
    for row in seats_map:
        for col in row:
            if col == C["occupied"]:
                count += 1

    print(f"Occupied seats (after {iterations} iters): {count}")


if __name__ == "__main__":
    main()
