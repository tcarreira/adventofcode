#!/usr/bin/env python3

from collections import deque
from pathlib import Path

curdir = Path(__file__).parent.absolute()


def play(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        card1, card2 = player1.popleft(), player2.popleft()

        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)


def parse_input(raw_input):
    input1, input2 = raw_input.split("\n\n")
    player1 = deque(map(int, input1.split("\n")[1:]))
    player2 = deque(map(int, input2.split("\n")[1:]))
    return player1, player2


def get_winner_score(player1, player2):
    winner = player1 if len(player2) == 0 else player2

    score = 0
    for c in range(1, len(winner) + 1):
        score += c * winner[-c]

    return score


def main():
    with open(curdir.joinpath("input.txt")) as f:
        raw_input = f.read().strip()

    player1, player2 = parse_input(raw_input)
    play(player1, player2)

    print(f"Solution: {get_winner_score(player1, player2)}")


if __name__ == "__main__":
    main()
