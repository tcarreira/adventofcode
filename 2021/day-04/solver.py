#!/usr/bin/env python3

from pathlib import Path
from typing import Tuple

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".strip()


def parse_input(p_input):
    raw_entries = p_input.split("\n\n")
    numbers_drawn = [x for x in raw_entries[0].split(",")]
    raw_boards = raw_entries[1:]

    boards = []
    for raw_board in raw_boards:
        boards.append([line.strip().split() for line in raw_board.strip().split("\n")])

    return numbers_drawn, boards


def print_board(board):
    print("\n".join([" ".join([f"{n:>2s}" for n in line]) for line in board]))


def check_bingo(boards):
    for i, board in enumerate(boards):
        for line in board:
            if line == ["x"] * 5:
                return board, i

        for column in zip(*board):
            if list(column) == ["x"] * 5:
                return board, i
    return None, None


def get_score(number, board):
    tmp_score = sum([sum([int(n) for n in line if n != "x"]) for line in board])
    # print(f"temp_score = {tmp_score}")
    return tmp_score * int(number)


def part1(numbers, boards):
    for number in numbers:
        boards = [
            [["x" if n == number else n for n in line] for line in board]
            for board in boards
        ]
        won_board, _ = check_bingo(boards)
        if won_board:
            # print_board(won_board)
            return get_score(number, won_board)


def part2(numbers, boards):
    for i, number in enumerate(numbers):
        # print(f"=========== {i}: {number} ")
        # for j, board in enumerate(boards):
        #     print("board", j)
        #     print_board(board)

        boards = [
            [["x" if n == number else n for n in line] for line in board]
            for board in boards
        ]

        if len(boards) == 1:
            return get_score(number, boards[0])

        # this while covers multiple wins during the same call
        while True:
            won_board, board_idx = check_bingo(boards)
            if won_board:
                boards.pop(board_idx)
                continue
            break


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input

    print("Solution to Part 1:")
    print(part1(*parse_input(raw_input)))

    print("Solution to Part 2:")
    print(part2(*parse_input(raw_input)))


if __name__ == "__main__":
    main()
