#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


def convert_binary(s, low="0", high="1"):
    exp = len(s)
    value = 0
    for c in s:
        exp -= 1
        if c == high:
            value += 2 ** exp
    return value


def convert_binary_to_seat(binary_str):
    row = convert_binary(binary_str[:7], low="F", high="B")
    column = convert_binary(binary_str[7:], low="L", high="R")

    return row, column


def convert_seat_to_id(seat):
    return seat[0] * 8 + seat[1]


def convert_ticket_to_id(ticket_str):
    seat = convert_binary_to_seat(ticket_str)
    return convert_seat_to_id(seat)


def main():
    with open(curdir + "/input.txt") as f:
        document = {}
        max_id = 0

        for line in f.readlines():
            id = convert_ticket_to_id(line.strip())
            if id > max_id:
                max_id = id

    print(f"highest seat ID: {max_id}")


if __name__ == "__main__":
    main()