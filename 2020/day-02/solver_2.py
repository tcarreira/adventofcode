#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))


with open(curdir + "/input.txt") as f:
    valid_passwords_count = 0

    # O(n)
    for line in f.readlines():
        match = re.search("([0-9]+)-([0-9]+) ([a-z]): (.*)", line.strip())

        position_1 = int(match.group(1)) - 1
        position_2 = int(match.group(2)) - 1
        character = match.group(3)
        password = match.group(4)

        if len(password) <= position_2:
            continue

        pass_char1 = password[position_1]
        pass_char2 = password[position_2]

        # Only one should match
        if pass_char1 != pass_char2 and (
            character == pass_char1 or character == pass_char2
        ):
            valid_passwords_count += 1

    print(f"Valid passwords: {valid_passwords_count}")
