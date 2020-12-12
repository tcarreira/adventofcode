#!/usr/bin/env python3

import os
from collections import defaultdict

curdir = os.path.dirname(os.path.realpath(__file__))


def count_configurations(adapters):
    # not mine :'(
    path = {0: 1}
    for r in adapters:
        path[r] = path.get(r - 3, 0)
        path[r] += path.get(r - 2, 0)
        path[r] += path.get(r - 1, 0)

    return path[adapters[-1]]


def main():
    adapters = [0]
    with open(curdir + "/input.txt") as f:
        for line in f.readlines():
            adapters.append(int(line.strip()))

    adapters.sort()
    adapters.append(adapters[-1] + 3)  # device +3 than highest adapter

    solution = count_configurations(adapters[1:])

    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
