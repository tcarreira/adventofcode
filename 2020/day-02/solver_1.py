#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))


with open(curdir + "/input.txt") as f:
    valid_passwords_count = 0

    # O(n)
    for line in f.readlines():
        match = re.search("([0-9]+)-([0-9]+) ([a-z]): (.*)", line.strip())

        lower_limit = int(match.group(1))
        higher_limit = int(match.group(2))
        character = match.group(3)
        password = match.group(4)

        count = len([c for c in password if c == character])

        if count >= lower_limit and count <= higher_limit:
            valid_passwords_count += 1

    print(f"Valid passwords: {valid_passwords_count}")
