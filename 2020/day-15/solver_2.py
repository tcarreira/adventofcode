#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(curdir + "/input.txt") as f:
        numbers = [int(x) for x in f.readline().strip().split(",")]

    memory = {n: i for i, n in enumerate(numbers[0:-1])}  # don't append last one

    i = len(numbers)
    while i < 30000000:
        if numbers[i - 1] in memory:
            numbers.append(i - memory[numbers[i - 1]] - 1)
        else:
            numbers.append(0)

        memory[numbers[i - 1]] = i - 1
        i += 1

    print(f"Solution: {numbers[-1]}")


if __name__ == "__main__":
    main()
