#!/usr/bin/env python3

import re
from pathlib import Path

curdir = Path(__file__).parent.absolute()


class I(int):
    def __add__(self, val):
        return I(super().__mul__(val))

    def __mul__(self, val):
        return I(super().__add__(val))


def calculate(expression):
    custom_num = re.sub(r"([0-9]+)", r"I(\1)", expression)
    custom_expression = custom_num.replace("+", "ß").replace("*", "+").replace("ß", "*")
    return eval(custom_expression)


def main():
    sum_values = 0
    with open(curdir.joinpath("input.txt")) as f:
        for line in f.readlines():
            sum_values += calculate(line)

    print(f"Solution: {sum_values}")


if __name__ == "__main__":
    main()
