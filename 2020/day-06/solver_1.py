#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))

_a = ord("a")


def letter_to_number(letter):
    return ord(letter.lower()) - _a


def main():
    with open(curdir + "/input.txt") as f:
        group_answers = [False] * 26
        sum_of_counts = 0

        for line in f.readlines():
            if line.strip() == "":
                group_count = len([a for a in group_answers if a])
                sum_of_counts += group_count
                
                group_answers = [False] * 26
            else:
                for c in line.strip():
                    group_answers[letter_to_number(c)] = True

        # last row
        group_count = len([a for a in group_answers if a])
        sum_of_counts += group_count
        group_answers = [False] * 26

    print(f"Sum of counts: {sum_of_counts}")


if __name__ == "__main__":
    main()