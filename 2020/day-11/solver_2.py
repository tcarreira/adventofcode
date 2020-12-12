#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))

C = {
    "empty": "L",
    "occupied": "#",
    "floor": ".",
}


def look_next_seat(seats_map, position, direction):
    i, j = direction
    row = position[0] + i
    col = position[1] + j

    while (
        0 <= row < len(seats_map)
        and 0 <= col < len(seats_map[0])
        and seats_map[row][col] == C["floor"]
    ):
        row += i
        col += j

    if 0 <= row < len(seats_map) and 0 <= col < len(seats_map[0]):
        return seats_map[row][col]

    return None


def get_new_cell(seats_map, row, col):
    if seats_map[row][col] == C["floor"]:
        return C["floor"]

    count = 0
    for direction in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        if (
            seats_map[row][col] != C["floor"]
            and look_next_seat(seats_map, (row, col), direction) == C["occupied"]
        ):
            count += 1

    if seats_map[row][col] == C["empty"] and count == 0:
        return C["occupied"]
    if seats_map[row][col] == C["occupied"] and count >= 5:
        return C["empty"]
    return seats_map[row][col]


def map_iteration(seats_map):
    new_map = []
    changes = 0
    for i, row in enumerate(seats_map):
        new_map.append("")
        for j, cell in enumerate(row):
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
