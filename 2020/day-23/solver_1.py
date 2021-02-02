#!/usr/bin/env python3

from pathlib import Path

curdir = Path(__file__).parent.absolute()


def simulate(numbers, moves, idx=0, picked=3):
    nlen = len(numbers)
    for k in range(moves):
        print(k, [ x+1 for x in numbers])

        current = numbers[idx]
        original_numbers = numbers
        moving = []
        for i in range(picked):
            moving.append(numbers[(idx + i + 1) % nlen])

        if idx < nlen - picked - 1:
            numbers = [*numbers[: idx + 1], *numbers[idx + picked + 1 :]]
        else:
            numbers = numbers[(idx + picked + 1) % nlen : idx + 1]

        destination_label = (current - 1) % nlen
        while destination_label in moving:
            destination_label = (destination_label - 1) % nlen
        destination = numbers.index(destination_label)

        for i, val in enumerate(moving):
            numbers.insert(destination + i + 1, val)

        idx = (numbers.index(current) + 1) % nlen

    return numbers

def main():
    with open(curdir.joinpath("input.txt")) as f:
        numbers = [int(x) - 1 for x in f.read().strip()]

    numbers = simulate(numbers, 100)

    one = numbers.index(0)
    numbers = [*numbers[one+1:], *numbers[:one]]

    result = "".join([str(x + 1) for x in numbers])
    print(f"Solution: {result}")


if __name__ == "__main__":
    main()
