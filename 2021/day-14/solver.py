#!/usr/bin/env python3

from pathlib import Path
from collections import Counter

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


def part1(p_input):
    sequence = p_input[0]
    rules_list = [line.split(" -> ") for line in [l for l in p_input[1].splitlines()]]
    rules = {rule[0]: rule[1] for rule in rules_list}

    for _ in range(10):
        next_sequence = sequence[0]  # first char
        for i in range(len(sequence) - 1):
            pair = sequence[i : i + 2]
            if pair in rules:
                next_sequence += f"{rules[pair]}{pair[1]}"
        sequence = next_sequence
    c = Counter(sequence).most_common()
    return c[0][1] - c[-1][1]


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    parts = [part for part in raw_input.split("\n\n")]

    print("Solution to Part 1:")
    print(part1(parts))


if __name__ == "__main__":
    main()
