#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


desired_sum = 2020

def build_numbers_dict():
    seen_numbers = {}  # space: O(n)
    with open(curdir + "/input.txt") as f:
        # O(n)
        for line in f.readlines():
            number = int(line)
            seen_numbers[number] = True
    return seen_numbers

def solve(numbers_dict):
    # O(N^2)
    for first_number in numbers_dict:
        tmp_sum = desired_sum - first_number

        # O(n)
        for second_number in numbers_dict:

            # O(1)
            if (tmp_sum - second_number) in numbers_dict:
                match_number = tmp_sum - second_number
                solution = first_number * second_number * match_number

                print(f"Found {first_number} + {second_number} + {match_number} = 2020")
                print(f"solution is: {solution}")
                return

solve(build_numbers_dict())
