#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip()


def part1(p_input):
    determ_die = list(map(lambda x: x % 100 + 1, range(103)))
    turn, player, score, state = 0, 1, {1: 0, 2: 0}, p_input
    while True:
        die_idx = (turn * 3) % 100
        turn += 1

        dice_sum = sum(determ_die[die_idx : die_idx + 3])
        state[player] = (state[player] + dice_sum - 1) % 10 + 1
        score[player] += state[player]

        # print(
        #     f"Turn {turn}, Player {player} rolls",
        #     determ_die[die_idx : die_idx + 3],
        #     "and moves to space",
        #     state[player],
        #     "with a score of",
        #     score[player],
        # )

        if score[player] >= 1000:
            return turn * 3 * score[(player % 2) + 1]

        player = (player % 2) + 1


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    players = {i + 1: int(l[-1]) for i, l in enumerate(raw_input.splitlines())}

    print("Solution to Part 1:")
    print(part1(players))


if __name__ == "__main__":
    main()
