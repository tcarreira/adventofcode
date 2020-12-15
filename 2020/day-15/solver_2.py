#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


def solution(numbers, until=2020):
    memory = {n: i + 1 for i, n in enumerate(numbers[:-1])}

    for i in range(len(numbers), until):
        numbers.append(i - memory.get(numbers[-1], i))
        memory[numbers[-2]] = i

    return numbers[-1]


def main():
    with open(curdir + "/input.txt") as f:
        numbers = [int(x) for x in f.readline().strip().split(",")]

    # print(f"Solution part 1: {solution(numbers, 2020)}")
    print(f"Solution part 2: {solution(numbers, 30000000)}")


if __name__ == "__main__":
    main()
