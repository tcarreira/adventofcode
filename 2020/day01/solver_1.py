#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


desired_sum = 2020
seen_numbers = {}

with open(curdir + "/input.txt") as f:

    # O(n)
    for line in f.readlines():
        number = int(line)

        # O(1)
        if (desired_sum - number) in seen_numbers:
            match_number = desired_sum - number
            solution = number * match_number

            print(f"Found {number} and {match_number}")
            print(f"solution is: {solution}")
            break
        else:
            # O(1)
            seen_numbers[number] = True
