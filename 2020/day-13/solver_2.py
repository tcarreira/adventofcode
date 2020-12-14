#!/usr/bin/env python3

import os
from math import prod

curdir = os.path.dirname(os.path.realpath(__file__))


# not mine =(
def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


def main():
    with open(curdir + "/input.txt") as f:
        buses = []
        indexes = []

        _ = f.readline()
        for i, c in enumerate(f.readline().split(",")):
            if c != "x":
                buses.append(int(c))
                indexes.append(int(c) - i)

    crt = chinese_remainder(buses, indexes)
    print(f"Solution: {crt}")


if __name__ == "__main__":
    main()
