#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))
mem = {}


def combinatorial(mask, address, addresses={}, i=0):
    if i >= len(mask):
        return
    if mask[len(mask) - 1 - i] == "X":
        addresses[address] = address
        combinatorial(mask, address, addresses, i + 1)
        addresses[address ^ (2 ** i)] = address ^ (2 ** i)
        combinatorial(mask, address ^ (2 ** i), addresses, i + 1)
    else:
        combinatorial(mask, address, addresses, i + 1)

    return addresses


def apply_mask(value, mask):
    ones_mask = int("".join(["0" if b!="1" else "1" for b in mask]), base=2)
    return (value|ones_mask)


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

                mem_addr = apply_mask(mem_addr, mask)
                addresses = combinatorial(mask, mem_addr, {})
                for address in addresses:
                    mem[address] = value

    solution = sum([v for v in mem.values()])
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
