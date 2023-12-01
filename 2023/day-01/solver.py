#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()
test_input2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()


# Fri Dec  1 19:19:06 WET 2023  --->  Fri Dec  1 19:23:01 WET 2023
# '0:03:55'
def part1(p_input):
    numbers = []
    for l in p_input:
        digits = [c for c in l if c in "0123456789"]
        numbers.append(int(digits[0] + digits[-1]))
    solution = sum(numbers)
    return solution


# Fri Dec  1 19:19:06 WET 2023  --->  Fri Dec  1 19:53:33 WET 2023
# '0:34:27'
def part2(p_input):
    numbers = []
    for l in p_input:
        l = l.replace("one", "one1one")
        l = l.replace("two", "two2two")
        l = l.replace("three", "three3three")
        l = l.replace("four", "four4four")
        l = l.replace("five", "five5five")
        l = l.replace("six", "six6six")
        l = l.replace("seven", "seven7seven")
        l = l.replace("eight", "eight8eight")
        l = l.replace("nine", "nine9nine")

        digits = [c for c in l if c in "0123456789"]
        numbers.append(int(digits[0] + digits[-1]))

    solution = sum(numbers)
    #  54145 too low
    #  54208 too low
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    p_input = [line for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(p_input))

    # raw_input = test_input2  # testing with the example - comment for real input
    # p_input = [line for line in raw_input.splitlines()]
    print("Solution to Part 2:")
    print(part2(p_input))


if __name__ == "__main__":
    main()
