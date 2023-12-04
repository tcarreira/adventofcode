#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


# Mon Dec  4 08:22:55 UTC 2023  --> Mon Dec  4 08:36:57 UTC 2023
# 0:14:02
def part1(p_input):
    solution = 0
    for card in p_input:
        wd = card.split(": ")[1]
        win = [int(x.strip()) for x in wd.split(" | ")[0].split(" ") if x != ""]
        drawn = [int(x.strip()) for x in wd.split(" | ")[1].split(" ") if x != ""]

        comm = len(set(win) & set(drawn))
        if (comm) > 0:
            solution += 2 ** ((comm) - 1)

    return solution


# Mon Dec  4 08:22:55 UTC 2023  --> Mon Dec  4 08:48:20 UTC 2023
# 0:25:25
def part2(p_input):
    solution = 0
    idx = -1
    cards = [l for l in p_input]
    multipliers = [1] * len(cards)
    while True:
        idx += 1
        if idx >= len(cards):
            break
        card = cards[idx]

        wd = card.split(": ")[1]
        win = [int(x.strip()) for x in wd.split(" | ")[0].split(" ") if x != ""]
        drawn = [int(x.strip()) for x in wd.split(" | ")[1].split(" ") if x != ""]

        comm = len(set(win) & set(drawn))
        for i in range(comm):
            multipliers[idx + 1 + i] += multipliers[idx]
        # solution+= multipliers[idx]*comm
    solution = sum(multipliers)
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
