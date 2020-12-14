#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(curdir + "/input.txt") as f:
        earliest = int(f.readline().strip())
        buses = [int(b) for b in f.readline().split(",") if b != "x"]

    next_bus_table = map(lambda id: ((earliest // id + 1) * id, id), buses)
    next_dep = min(next_bus_table)

    print(f"Next departure: {next_dep[0]}")
    print(f"Answer: {(next_dep[0] - earliest) * next_dep[1]}")


if __name__ == "__main__":
    main()
