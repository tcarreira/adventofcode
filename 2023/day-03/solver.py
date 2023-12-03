#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


def check_cell(matrix, x, y, sub_call=False):
    try:
        if matrix[y][x] == ".":
            return False
    except:
        return False

    # xxx
    # xO.
    # ...
    for coor in [(y - 1, x - 1), (y, x - 1), (y - 1, x), (y - 1, x + 1)]:
        if (
            coor[0] < 0
            or coor[0] >= len(matrix)
            or coor[1] < 0
            or coor[1] >= len(matrix[0])
        ):
            continue
        cell = matrix[coor[0]][coor[1]]
        if sub_call and (not cell.isdigit() and cell != "."):
            return True
        elif not sub_call and (cell.isdigit() or cell != "."):
            return True

    # ...
    # .Ox
    # xxx
    for coor in [(y, x), (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]:
        if (
            coor[0] < 0
            or coor[0] >= len(matrix)
            or coor[1] < 0
            or coor[1] >= len(matrix[0])
        ):
            continue
        cell = matrix[coor[0]][coor[1]]
        if not cell.isdigit() and cell != ".":
            return True

    return check_cell(matrix, x + 1, y, sub_call=True)

# Sun Dec  3 15:36:46 UTC 2023 --> Sun Dec  3 16:19:13 UTC 2023
# 0:42:27
def part1(p_input):
    matrix = []
    for line in p_input:
        matrix.append([c for c in line])

    for y, l in enumerate(matrix):
        for x, c in enumerate(l):
            if not check_cell(matrix, x, y):
                matrix[y][x] = "."

    for x, l in enumerate(matrix):
        for y, c in enumerate(l):
            if not c.isdigit():
                matrix[x][y] = "."

    solution = 0
    for line in matrix:
        numbers = [
            int(n) for n in "".join(line).split(".") if len(n) > 0 and n.isdigit()
        ]
        solution += sum(numbers)

    return solution


# Sun Dec  3 15:36:46 UTC 2023 --> Sun Dec  3 16:54:16 UTC 2023
# 1:17:30
def part2(p_input):
    matrix = []
    solution = 0
    for line in p_input:
        matrix.append([c for c in line])

    for y, l in enumerate(matrix):
        for x, c in enumerate(l):
            if not check_cell(matrix, x, y):
                matrix[y][x] = "."

    for y, l in enumerate(matrix):
        for x, c in enumerate(l):
            if c != "*":
                continue

            left = matrix[y][max(0, x - 4) : max(0, x)]
            right = matrix[y][min(len(matrix[y]), x + 1) : min(len(matrix[y]), x + 4)]
            up = matrix[max(0, y - 1)][max(0, x - 3) : min(len(matrix[y]), x + 4)]
            down = matrix[min(len(matrix), y + 1)][
                max(0, x - 3) : min(len(matrix[y]), x + 4)
            ]

            parts = []
            if left[-1].isdigit():
                parts.append(int("".join(left).split(".")[-1]))
            if right[0].isdigit():
                parts.append(int("".join(right).split(".")[0]))

            if up[2].isdigit() or up[3].isdigit() or up[4].isdigit():
                digit = True
                for z in range(4, 7):
                    if digit:
                        if not up[z].isdigit():
                            digit = False
                    if not digit:
                        if up[z].isdigit():
                            up[z] = "."

                digit = True
                for z in range(2, -1, -1):
                    if digit:
                        if not up[z].isdigit():
                            digit = False
                    if not digit:
                        if up[z].isdigit():
                            up[z] = "."

                up = [u if u.isdigit() else "." for u in up]
                ups = [int(n) for n in "".join(up).split(".") if n != ""]
                for u in ups:
                    parts.append(u)

            if down[2].isdigit() or down[3].isdigit() or down[4].isdigit():
                digit = True
                for z in range(4, 7):
                    if digit:
                        if not down[z].isdigit():
                            digit = False
                    if not digit:
                        if down[z].isdigit():
                            down[z] = "."

                digit = True
                for z in range(2, -1, -1):
                    if digit:
                        if not down[z].isdigit():
                            digit = False
                    if not digit:
                        if down[z].isdigit():
                            down[z] = "."

                down = [d if d.isdigit() else "." for d in down]
                downs = [int(n) for n in "".join(down).split(".") if n != ""]
                for d in downs:
                    parts.append(d)

            if len(parts) == 2:
                solution += parts[0] * parts[1]
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
