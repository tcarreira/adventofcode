#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict, deque

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()


def part1(p_input):
    current_cost, visited = 0, {(0, 0)}
    cost_map = [[0] * len(p_input[0]) for _ in p_input]
    x_max, y_max = len(cost_map[0]), len(cost_map)
    next_positions = defaultdict(list)
    next_positions[0] = [((0, 1), 0), ((1, 0), 0)]

    while True:
        current_level = sorted(
            next_positions[current_cost], key=lambda p: p_input[p[0][1]][p[0][0]]
        )
        for pos, pos_cost in current_level:
            if pos in visited or pos_cost < current_cost:
                continue
            visited.add(pos)
            new_cost = pos_cost + p_input[pos[1]][pos[0]]
            cost_map[pos[1]][pos[0]] = new_cost
            for p in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_pos = (pos[0] + p[0], pos[1] + p[1])
                if (
                    0 <= new_pos[0] < x_max
                    and 0 <= new_pos[1] < y_max
                    and new_pos not in visited
                ):
                    next_positions[new_cost].append((new_pos, new_cost))

        current_cost += 1
        if max(next_positions.keys()) < current_cost:
            return cost_map[-1][-1]


def part2(p_input):
    max_x, max_y = len(p_input[0]), len(p_input)
    new_input = [[0] * max_x * 5 for _ in range(max_y * 5)]
    for y in range(5 * len(p_input)):
        for x in range(5 * len(p_input[0])):
            original_value = p_input[y % max_y][x % max_x]
            incremented_value = original_value + (y // max_y + x // max_x)
            new_input[y][x] = (incremented_value - 1) % 9 + 1

    solution = part1(new_input)
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    risk_map = [[int(c) for c in line] for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(risk_map))

    print("Solution to Part 2:")
    print(part2(risk_map))


if __name__ == "__main__":
    main()
