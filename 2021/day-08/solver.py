#!/usr/bin/env python3

from pathlib import Path
from collections import Counter

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input_1 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
test_input = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".strip()


def part1(p_input):
    solution = 0
    for line in p_input:
        for digit in line[1].split():
            if len(digit) in {2, 4, 3, 7}:
                solution += 1
    return solution


def part2(p_input):
    def translate(all_digit_str, my_digits_str):
        number_four = [segs for segs in all_digit_str.split() if len(segs) == 4][0]

        # each segment has a unique count (or appears only once in number four)
        mapping = {" ": " "}
        segment_count = Counter(all_digit_str.replace(" ", ""))
        for segment, count in segment_count.most_common():
            if count == 9:
                mapping[segment] = "f"
            elif count == 8:
                if segment in number_four:
                    mapping[segment] = "c"
                else:
                    mapping[segment] = "a"
            elif count == 7:
                if segment in number_four:
                    mapping[segment] = "d"
                else:
                    mapping[segment] = "g"
            elif count == 6:
                mapping[segment] = "b"
            elif count == 4:
                mapping[segment] = "e"
            else:
                print("Opppps...", segment, count)

        return "".join(mapping[x] for x in my_digits_str)

    def segments_to_number(digits_str):
        mapping = {
            "abcefg": 0,
            "cf": 1,
            "acdeg": 2,
            "acdfg": 3,
            "bcdf": 4,
            "abdfg": 5,
            "abdefg": 6,
            "acf": 7,
            "abcdefg": 8,
            "abcdfg": 9,
        }

        digits = [mapping["".join(sorted(x))] for x in digits_str.split()]
        return int("".join([str(d) for d in digits]))

    solution = 0
    for line in p_input:
        digits = translate(*line)
        solution += segments_to_number(digits)
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    numbers = [line.split(" | ") for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(numbers))

    print("Solution to Part 2:")
    print(part2(numbers))


if __name__ == "__main__":
    main()
