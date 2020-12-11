#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))


class Instruction:
    def __init__(self, line, oper, arg):
        self.line = line
        self.oper = oper
        self.arg = arg


def run(instructions):
    accumulator = 0
    last_pc=0
    pc = 0
    visited = [False] * len(instructions)

    while pc < len(instructions) and not visited[pc]:
        last_pc=pc
        inst = instructions[pc]
        visited[pc] = True
        if inst.oper == "acc":
            accumulator += int(inst.arg)
        elif inst.oper == "jmp":
            pc += int(inst.arg)
            continue
        elif inst.oper == "nop":
            pass
        pc += 1

    return last_pc == len(instructions)-1, accumulator


def read_instructions(filepath):
    instructions = []
    with open(filepath) as f:
        i = 0
        for line in f.readlines():
            op, arg = line.strip().split(" ", maxsplit=1)
            instructions.append(Instruction(i, op, arg))
    return instructions


def main():
    instructions = read_instructions(curdir + "/input.txt")
    _, accumulator = run(instructions)

    print(f"Accumulator Value before loop: {accumulator}")


if __name__ == "__main__":
    main()