#!/usr/bin/env python3

import os
from collections import defaultdict

curdir = os.path.dirname(os.path.realpath(__file__))


def get_jump_counts(adapters):
    jumps = defaultdict(lambda: 0)
    for i in range(1, len(adapters)):
        jump = adapters[i] - adapters[i - 1]
        jumps[jump] += 1
    return jumps


def main():
    adapters = [0]
    with open(curdir + "/input.txt") as f:
        for line in f.readlines():
            adapters.append(int(line.strip()))

    adapters.sort()
    adapters.append(adapters[-1] + 3)  # device +3 than highest adapter

    jumps = get_jump_counts(adapters)
    print(f"1-step jumps: {jumps[1]}")
    print(f"3-step jumps: {jumps[3]}")
    print(f"Solution: {jumps[1] * jumps[3]}")


if __name__ == "__main__":
    main()
