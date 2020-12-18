#!/usr/bin/env python3

import re
from pathlib import Path

curdir = Path(__file__).parent.absolute()


OPERS = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}


def find_parenthesis_expression(elements):
    par = 1
    i = 0
    while par > 0 and i < len(elements):
        i += 1
        if elements[i] == "(":
            par += 1
        elif elements[i] == ")":
            par -= 1
    return elements[1:i], i


def calculate_expression(elements):
    result = 0
    operation = OPERS["+"]
    i = 0
    while i < len(elements):
        if elements[i] == "(":
            inner_exp, index = find_parenthesis_expression(elements[i:])
            result = operation(result, calculate_expression(inner_exp))
            i += index + 1
            continue
        elif elements[i] in OPERS:
            operation = OPERS[elements[i]]
        elif elements[i] == "":
            pass
        else:
            number = int(elements[i])
            result = operation(result, number)
        i += 1
    return result


def main():
    sum_values = 0
    with open(curdir.joinpath("input.txt")) as f:
        for line in f.readlines():
            sum_values += calculate_expression(
                re.split("(\W)", line.strip().replace(" ", ""))
            )

    print(f"Solution: {sum_values}")


if __name__ == "__main__":
    main()
