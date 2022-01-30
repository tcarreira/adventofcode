#!/usr/bin/env python3

from functools import lru_cache
from pathlib import Path
from typing import Dict, Tuple

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip()


def part1(p_input: Dict[int, int]):
    p_input = {k: v for k, v in p_input.items()}
    determ_die = list(map(lambda x: x % 100 + 1, range(103)))
    turn, player, score, state = 0, 1, {1: 0, 2: 0}, p_input
    while True:
        die_idx = (turn * 3) % 100
        turn += 1

        dice_sum = sum(determ_die[die_idx : die_idx + 3])
        state[player] = (state[player] + dice_sum - 1) % 10 + 1
        score[player] += state[player]

        if score[player] >= 1000:
            return turn * 3 * score[(player % 2) + 1]

        player = (player % 2) + 1


@lru_cache(None)
def dirac_dice(
    score: Tuple[int, int],
    board: Tuple[int, int],
    player: int,
    move: int,
) -> Tuple[int, int]:

    # move player
    new_board = (
        ((board[0] + (move if player == 0 else 0)) - 1) % 10 + 1,
        ((board[1] + (move if player == 1 else 0)) - 1) % 10 + 1,
    )

    new_score = (
        score[0] + (new_board[0] if player == 0 else 0),
        score[1] + (new_board[1] if player == 1 else 0),
    )

    if new_score[0] >= 21:
        return (1, 0)
    if new_score[1] >= 21:
        return (0, 1)

    total_score = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                next_move = d1 + d2 + d3
                tmp_score = dirac_dice(
                    score=new_score,
                    board=new_board,
                    player=int(not (player)),
                    move=next_move,
                )
                total_score = (
                    total_score[0] + tmp_score[0],
                    total_score[1] + tmp_score[1],
                )

    return total_score


def part2(p_input: Dict[int, int]):
    score = (0, 0)
    board = (p_input[1], p_input[2])

    # cache = {}
    total_score = (0, 0)

    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                next_move = d1 + d2 + d3
                tmp_score = dirac_dice(
                    score=score, board=board, player=0, move=next_move
                )
                total_score = (
                    total_score[0] + tmp_score[0],
                    total_score[1] + tmp_score[1],
                )
    return max(total_score)


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    players = {i + 1: int(l[-1]) for i, l in enumerate(raw_input.splitlines())}

    print("Solution to Part 1:")
    print(part1(players))

    print("Solution to Part 2:")
    print(part2(players))


if __name__ == "__main__":
    main()
