#!/usr/bin/env python3

from pathlib import Path
import re
import math

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".strip()


class Snumber:
    @classmethod
    def _parse_parcial_number(cls, string: str) -> str:
        match = re.match(r"([0-9]+)", string)
        if match:
            return match.group(0), len(match.group(0))
        stack, i = ["["], 1
        while len(stack) > 0:
            if string[i] == "[":
                stack.append("[")
            elif string[i] == "]":
                stack.pop()
            i += 1
        return string[:i], i

    def __init__(self, string: str) -> None:
        if string[0] == "[":
            left, i = Snumber._parse_parcial_number(string[1:])
            right, _ = Snumber._parse_parcial_number(string[i + 2 :])
            self.left = Snumber(left)
            self.right = Snumber(right)
            self.value = None
        else:
            self.left = None
            self.right = None
            self.value = int(string)

    def magnitude(self, carry: int = 0) -> int:
        if self.value is not None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def _explode(
        self, level=1, has_exploded=False, to_l=None, to_r=None
    ) -> tuple[bool, int, int]:
        if to_r is not None:  # handle explosion to the right
            if self.value is not None:
                self.value += to_r
            else:
                self.left._explode(to_l=to_l, to_r=to_r)
            return True, to_l, None
        if to_l is not None:  # handle explosion to the left
            if self.right is None:
                self.value += to_l
            else:
                self.right._explode(to_l=to_l)
            return True, None, None

        if has_exploded:
            return True, None, None

        if self.value is None:
            if level > 4:
                # Explosion
                l, r = self.left.value, self.right.value
                self.value, self.left, self.right = 0, None, None
                return True, l, r

            has_exploded, l, r = self.left._explode(level + 1)
            if l is not None:
                if r is not None:  # This node just exploded, pass to_left
                    self.right._explode(has_exploded=True, to_r=r)
                return True, l, None  # pass explosion to left

            has_exploded, l, r = self.right._explode(
                level + 1, has_exploded=has_exploded, to_r=r
            )
            if r is not None:
                if l is not None:  # This node just exploded, pass to_left
                    self.left._explode(has_exploded=True, to_l=l)
                return True, None, r  # pass explosion to right

            if l is not None:
                self.left._explode(has_exploded=True, to_l=l)
            return has_exploded, None, None

        return False, None, None

    def _split(self) -> bool:
        if self.value is not None:
            if self.value > 9:
                self.left = Snumber(str(math.floor(self.value / 2)))
                self.right = Snumber(str(math.ceil(self.value / 2)))
                self.value = None
                return True
        else:
            if self.left._split():
                return True
            return self.right._split()

    def reduce(self) -> "Snumber":
        # print(f"      starting, {self}")
        while True:
            while True:
                has_exploded, _, _ = self._explode()
                # print(f"after explodes, {self}")
                if not has_exploded:
                    break

            has_splitted = self._split()
            # print("++ after split:", self)
            if not has_splitted:
                break
        return self

    def __str__(self) -> str:
        if self.value is not None:
            return str(self.value)
        else:
            return f"[{self.left},{self.right}]"


def part1(p_input):
    a = Snumber(p_input[0])
    for number_str in p_input[1:]:
        b = Snumber(number_str)
        tmp_sum = Snumber(f"[{a},{b}]")
        a = tmp_sum.reduce()
        # a = tmp_sum

    return a.magnitude()


def part2(p_input):
    all_sums = []
    for a in p_input:
        for b in p_input:
            if a != b:
                all_sums.append(f"[{a},{b}]")

    magnitudes = [Snumber(sn).reduce().magnitude() for sn in all_sums]
    solution = max(magnitudes)
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    numbers = raw_input.splitlines()

    print("Solution to Part 1:")
    print(part1(numbers))

    print("Solution to Part 2:")
    print(part2(numbers))


if __name__ == "__main__":
    main()
