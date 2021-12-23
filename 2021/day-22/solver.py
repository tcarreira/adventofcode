#!/usr/bin/env python3

from pathlib import Path
import re
from collections import defaultdict

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
""".strip()


class Instruction:
    def __init__(self, instruction: str) -> None:
        matched = re.match(
            r"(on|off) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)",
            instruction,
        )
        self.switch = matched.group(1)
        self.set_value = 1 if self.switch == "on" else 0
        self.min_x = int(matched.group(2))
        self.max_x = int(matched.group(3))
        self.min_y = int(matched.group(4))
        self.max_y = int(matched.group(5))
        self.min_z = int(matched.group(6))
        self.max_z = int(matched.group(7))
        self.x = range(self.min_x, self.max_x + 1)
        self.y = range(self.min_y, self.max_y + 1)
        self.z = range(self.min_z, self.max_z + 1)


def part1(p_input):
    instructions = [Instruction(instruction_str) for instruction_str in p_input]
    on_cells = defaultdict(int)

    for i, instr in enumerate(instructions):
        # print("instruction", i)
        if (
            instr.min_x < -50
            or instr.max_x > 50
            or instr.min_y < -50
            or instr.max_y > 50
            or instr.min_z < -50
            or instr.max_z > 50
        ):
            continue
        for x in instr.x:
            for y in instr.y:
                for z in instr.z:
                    on_cells[(x, y, z)] = instr.set_value

    solution = sum(on_cells.values())
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    raw_input = test_input  # testing with the example - comment for real input
    instructions = raw_input.splitlines()

    print("Solution to Part 1:")
    print(part1(instructions))


if __name__ == "__main__":
    main()
