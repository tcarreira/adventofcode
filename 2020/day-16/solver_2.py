#!/usr/bin/env python3

import inspect
import re
from pathlib import Path

curdir = Path(__file__).parent.absolute()


def parse_rules(input_rules):
    all_rules = {}
    for in_rule in input_rules.split("\n"):
        match = re.match(r"(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+).*", in_rule)
        field = match.group(1)
        min1, max1 = int(match.group(2)), int(match.group(3))
        min2, max2 = int(match.group(4)), int(match.group(5))

        all_rules[field] = get_lambda(min1, max1, min2, max2)
    return all_rules


def get_rules_mapping_possible_indexes(all_rules, nearby_tickets):
    # each field starts by mapping to all available positions
    rules_mapping = {field: set(i for i in range(len(all_rules))) for field in all_rules}

    # iterate all tickets (including invalid)
    for ticket in nearby_tickets.split("\n")[1:-1]:
        ticket_values = [int(val) for val in ticket.split(",")]

        # check only valid tickets
        if all(any([rule(v) for rule in all_rules.values()]) for v in ticket_values):
            # for every non-matching rule, discard its index from rules_mapping
            for i, val in enumerate(ticket_values):
                pass
                for field, rule in all_rules.items():
                    if not rule(val):
                        rules_mapping[field].remove(i)
    return rules_mapping


def build_final_mapping(sorted_rules):
    # build final_map. For each mapped field, discard index from other fields
    final_map = {}
    for i in range(len(sorted_rules)):
        index = sorted_rules[i][1].pop()
        final_map[sorted_rules[i][0]] = index
        for j in range(i, len(sorted_rules)):
            sorted_rules[j][1].discard(index)
    return final_map


# closure
def get_lambda(min1, max1, min2, max2):
    return lambda v: min1 <= v <= max1 or min2 <= v <= max2


def main():
    # Parse 3 different input parts
    with open(curdir.joinpath("input.txt")) as f:
        in_rules, my_ticket, nearby_tickets = f.read().split("\n\n")

    all_rules = parse_rules(in_rules)

    rules_mapping = get_rules_mapping_possible_indexes(all_rules, nearby_tickets)

    # sort by less mapped indexes (start final_map by single-mapped indexes)
    sorted_rules = sorted(rules_mapping.items(), key=lambda x: len(x[1]))

    final_map = build_final_mapping(sorted_rules)

    # find my ticket fields starting with departure
    my_ticket = [int(i) for i in my_ticket.split("\n")[1].split(",")]
    answer = 1
    for field in [f for f in all_rules if f.startswith("departure")]:
        answer *= my_ticket[final_map[field]]

    print(f"Fields mapping: {final_map}")
    print(f"Solution: {answer}")


if __name__ == "__main__":
    main()
