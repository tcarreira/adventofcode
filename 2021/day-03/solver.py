#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    report = [line for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(report))

    print("Solution to Part 2:")
    print(part2(report))


def get_most_common(entries, current_bit):
    counts = {"0": 0, "1": 0}
    for entry in entries:
        counts[entry[current_bit]] += 1

    return int(counts["0"] <= counts["1"])


def calculate_level(p_input, is_co2=False):
    current_bit = 0
    entries = [x for x in p_input]
    while len(entries) > 1:
        bit = get_most_common(entries, current_bit)

        bit = bit if not is_co2 else int(not (bit))
        entries = [e for e in entries if e[current_bit] == str(bit)]
        current_bit += 1

    return entries[0]


def part1(p_input):
    bits = [0 for _ in p_input[0]]
    for current_bit, _ in enumerate(p_input[0]):
        bits[current_bit] = str(get_most_common(p_input, current_bit))

    gamma = "".join(bits)
    epsilon = gamma.translate({ord("0"): ord("1"), ord("1"): ord("0")})

    # print({"gamma": int(gamma, 2), "epsilon": int(epsilon, 2)})
    solution = int(gamma, 2) * int(epsilon, 2)
    return solution


def part2(p_input):

    oxygen_level = calculate_level(p_input, is_co2=False)
    co2_level = calculate_level(p_input, is_co2=True)

    # print({"oxygen": int(oxygen_level, 2), "co2": int(co2_level, 2)})
    return int(oxygen_level, 2) * int(co2_level, 2)


if __name__ == "__main__":
    main()
