#!/usr/bin/env python3

from pathlib import Path
import math

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()
test_2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip()


class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


# 0:11:40
def part1(p_input):
    instrs = p_input[0]
    tree = {}
    for l in p_input[2:]:
        v = l.split(" = ")[0]
        tree[v] = Node(v)

    for l in p_input[2:]:
        v, lr = l.split(" = ")
        l, r = lr[1:-1].split(", ")
        tree[v].l = l
        tree[v].r = r

    solution = 0
    curr = "AAA"
    while True:
        for instr in instrs:
            solution += 1
            if curr == "ZZZ":
                break

            if instr == "L":
                curr = tree[curr].l
            elif instr == "R":
                curr = tree[curr].r
            else:
                raise RuntimeError("unreach")
        if curr == "ZZZ":
            break

    return solution


# 0:41:00
def part2(p_input):
    instrs = p_input[0]
    tree = {}
    for l in p_input[2:]:
        v = l.split(" = ")[0]
        tree[v] = Node(v)

    for l in p_input[2:]:
        v, lr = l.split(" = ")
        l, r = lr[1:-1].split(", ")
        tree[v].l = l
        tree[v].r = r

    def rep_numbers(curr):
        reps = -1
        result = []
        seen = set()
        finish = False
        while True:
            for i, instr in enumerate(instrs):
                reps += 1
                if curr.endswith("Z"):
                    result.append(reps)

                if (curr, i) in seen:
                    finish = True
                    break
                seen.add((curr, i))

                if instr == "L":
                    curr = tree[curr].l
                elif instr == "R":
                    curr = tree[curr].r
                else:
                    raise RuntimeError("unreach")
            if finish:
                break
        return result

    ghosts_reps = [rep_numbers(x) for x in [t for t in tree if t.endswith("A")]]
    solution = math.lcm(*[min(x) for x in ghosts_reps])

    return solution
    # 28481839152814005834591031 too high


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input

    # simple treat input
    p_input = [line for line in raw_input.splitlines()]
    # p_input = [int(line) for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(p_input))

    # p_input = [line for line in test_2.splitlines()]

    print("Solution to Part 2:")
    print(part2(p_input))


if __name__ == "__main__":
    main()
