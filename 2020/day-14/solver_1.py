#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))
mem = {}

def apply_mask(value, mask):
    ones_mask = int("".join(["1" if b=="1" else "0" for b in mask]), base=2)
    zeros_mask = int("".join(["0" if b=="0" else "1" for b in mask]), base=2)

    return (value|ones_mask)&zeros_mask 


def main():
    with open(curdir + "/input.txt") as f:
        for line in f.readlines():
            if "mask" in line:
                match = re.match("mask = ([X01]+)", line.strip())
                mask = match.group(1)
                continue
            else:
                match = re.match("mem\[([0-9]+)\] = ([0-9]+)", line.strip())
                mem_addr = int(match.group(1))
                value = int(match.group(2))

                mem[mem_addr] = apply_mask(value, mask)

    solution = sum([v for v in mem.values()])
    print(f"Solution: {solution}")

if __name__ == "__main__":
    main()
