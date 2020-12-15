#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(curdir + "/input.txt") as f:
        numbers = [int(x) for x in f.readline().strip().split(",")]

    i = len(numbers)
    while i < 2020:
        for j in range(i - 2, -1, -1):
            if numbers[j] == numbers[i - 1]:
                numbers.append(i - j - 1)
                break
        else:
            numbers.append(0)
        i += 1

    print(f"Solution: {numbers[-1]}")


if __name__ == "__main__":
    main()
