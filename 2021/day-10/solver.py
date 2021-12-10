#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip()


def part1(p_input):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    chunk_match = {")": "(", "]": "[", "}": "{", ">": "<"}
    solution = 0
    for line in p_input:
        heap = []
        for c in line:
            if c in chunk_match.values():
                heap.append(c)
            elif chunk_match[c] == heap[-1]:
                heap.pop()
            else:
                solution += score_table[c]
                break

    return solution


def part2(p_input):
    score_table = {"(": 1, "[": 2, "{": 3, "<": 4}
    chunk_match = {")": "(", "]": "[", "}": "{", ">": "<"}

    def get_incomplete():
        incomplete = []
        for line in p_input:
            heap = []
            for c in line:
                if c in chunk_match.values():
                    heap.append(c)
                elif chunk_match[c] == heap[-1]:
                    heap.pop()
                else:
                    break
            else:
                incomplete.append(line)
        return incomplete

    def get_score(chunks):
        score = 0
        while len(chunks) > 0:
            c = chunks.pop()
            score = score * 5 + score_table[c]
        return score

    scores = []
    for line in get_incomplete():
        heap = []
        for c in line:
            if c in chunk_match.values():
                heap.append(c)
            elif chunk_match[c] == heap[-1]:
                heap.pop()
            else:
                print("Should not reach corruption")
                break
        scores.append(get_score(heap))

    solution = sorted(scores)[len(scores) // 2]
    return solution


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    lines = raw_input.splitlines()

    print("Solution to Part 1:")
    print(part1(lines))

    print("Solution to Part 2:")
    print(part2(lines))


if __name__ == "__main__":
    main()
