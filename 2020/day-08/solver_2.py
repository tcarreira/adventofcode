#!/usr/bin/env python3

import os
import re

from solver_1 import read_instructions, run

curdir = os.path.dirname(os.path.realpath(__file__))


def test_swap_operation(instructions, line):
    swapper = {"nop": "jmp", "jmp": "nop"}

    if instructions[line].oper not in swapper:
        return False, 0

    instructions[line].oper = swapper[instructions[line].oper]
    result = run(instructions)
    instructions[line].oper = swapper[instructions[line].oper]

    return result


def main():
    instructions = read_instructions(curdir + "/input.txt")

    i = 0
    while i < len(instructions):
        did_end, accumulator = test_swap_operation(instructions, i)
        if did_end:
            print(f"Accumulator Value before loop: {accumulator}")
            return
        i += 1



if __name__ == "__main__":
    main()