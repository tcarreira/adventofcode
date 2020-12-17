#!/usr/bin/env python3

import inspect
import re
from pathlib import Path

curdir = Path(__file__).parent.absolute()


# closure
def get_lambda(min1, max1, min2, max2):
    return lambda v: min1 <= v <= max1 or min2 <= v <= max2


def main():
    all_rules = []
    with open(curdir.joinpath("input.txt")) as f:
        in_rules, my_ticket, nearby_tickets = f.read().split("\n\n")

    for in_rule in in_rules.split("\n"):
        match = re.match(r"(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+).*", in_rule)
        min1, max1 = int(match.group(2)), int(match.group(3))
        min2, max2 = int(match.group(4)), int(match.group(5))

        all_rules.append(get_lambda(min1, max1, min2, max2))

    invalid_sum = 0
    for ticket in nearby_tickets.split("\n")[1:-1]:
        for val_str in ticket.split(","):

            for rule in all_rules:
                if rule(int(val_str)):
                    break
            else:
                invalid_sum += int(val_str)

    print(f"Solution: {invalid_sum}")


if __name__ == "__main__":
    main()
