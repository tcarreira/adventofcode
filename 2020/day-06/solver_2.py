#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))

_a = ord("a")


def letter_to_number(letter):
    return ord(letter.lower()) - _a


def main():
    with open(curdir + "/input.txt") as f:
        group_answers = [0] * 26
        group_count = 0
        sum_of_counts = 0

        for line in f.readlines():
            if line.strip() == "":
                group_count = len([a for a in group_answers if a == group_count])
                sum_of_counts += group_count

                group_answers = [0] * 26
                group_count = 0
            else:
                group_count += 1
                for c in line.strip():
                    group_answers[letter_to_number(c)] += 1

        group_count = len([a for a in group_answers if a == group_count])
        sum_of_counts += group_count

    print(f"Sum of counts: {sum_of_counts}")


if __name__ == "__main__":
    main()