#!/usr/bin/env python3

from pathlib import Path
from statistics import median

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = "16,1,2,0,4,2,7,1,2,14"


def part1(p_input):
    med = int(round(median(p_input), 0))
    solution = sum([abs(x - med) for x in p_input])
    return solution


def part2(p_input):
    # The fuel will be a triangular number (https://en.wikipedia.org/wiki/Triangular_number)
    def triang(n: int):
        return (n * (n + 1)) / 2

    # get the real maths, but brute force would be fast enough, I think
    # S = Σ (n) * (n + 1)) / 2  ;;; n = k - H ; Σ(i=1 -> n)
    # S = Σ (n^2 + n)) / 2  ;;; n = k - H
    # S = Σ ( (k - H)^2  + (k - H) ) /2
    # S = Σ ( (k^2 - 2kH + H^2 ) + (k - H) ) /2
    # S = Σ ( H^2  + (-2k - 1)*H + (k^2 + 1)  ) /2   # make derivative for H to find its min:
    # S' = Σ ( 2H - 2k - 1 ) / 2    #==> S' = 0
    # 0 = Σ 2H - 2k -1
    # 0 = 2ΣH - 2Σk - Σ1
    # 0 = 2nH - 2Σk - n
    # 2nH = 2Σk + n
    # H = (2Σk + n) / (2n)

    n = len(p_input)
    med = (2 * sum(p_input) + n) / (2 * n)

    # The formal calculation works for continuous values.
    #   In order to figure out the solution for descrete values,
    #   I'll search near the continuous solution
    one_of_this = [int(round(med - i)) for i in range(-2, 3)]

    #
    def how_much_fuel(position):
        return int(sum([triang(abs(x - position)) for x in p_input]))

    solution = min(how_much_fuel(pos) for pos in one_of_this)
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    numbers = [int(number) for number in raw_input.split(",")]

    print("Solution to Part 1:")
    print(part1(numbers))

    print("Solution to Part 2:")
    print(part2(numbers))


if __name__ == "__main__":
    main()
