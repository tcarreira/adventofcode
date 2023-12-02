#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()


def is_possible(line):
    available_cubes = {"red": 12, "green": 13, "blue": 14}
    subsets = line.split(": ")[1]
    for subset in subsets.split("; "):
        for draw in subset.split(", "):
            number, color = draw.split(" ")
            if int(number) > available_cubes[color]:
                return False
    return True


def get_power(line):
    max_seen = {"red": 0, "green": 0, "blue": 0}
    subsets = line.split(": ")[1]
    for subset in subsets.split("; "):
        for draw in subset.split(", "):
            number, color = draw.split(" ")
            max_seen[color] = max(int(number), max_seen[color])
    return max_seen["red"] * max_seen["green"] * max_seen["blue"]


# Sat Dec  2 21:04:35 UTC 2023  --->  Sat Dec  2 21:14:32 UTC 2023
# 0:09:57
def part1(p_input):
    possible_games = []
    for game, line in enumerate(p_input):
        # colors = {"red": 0, "blue": 0, "green": 0}
        if is_possible(line):
            possible_games.append(game + 1)

    solution = sum(possible_games)
    return solution


# Sat Dec  2 21:04:35 UTC 2023  --->  Sat Dec  2 21:18:57 UTC 2023
# 0:14:22
def part2(p_input):
    powers = []
    for line in p_input:
        # colors = {"red": 0, "blue": 0, "green": 0}
        powers.append(get_power(line))
    solution = sum(powers)
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
