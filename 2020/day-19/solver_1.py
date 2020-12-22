#!/usr/bin/env python3

import re
from collections import defaultdict
from pathlib import Path

curdir = Path(__file__).parent.absolute()


class Rule:
    def __init__(self):
        self.p1 = []
        self.p2 = []


def rules_to_regex(rule):
    if rule is None or rule.p1 is None:
        return ""
    if isinstance(rule.p1, str):
        return f"{rule.p1}"

    p1 = "".join([rules_to_regex(x) for x in rule.p1])
    if rule.p2 is None:
        return f"({p1})"

    p2 = "".join([rules_to_regex(x) for x in rule.p2])
    return f"({p1}|{p2})"


def main():
    rules = defaultdict(lambda: Rule())

    with open(curdir.joinpath("input.txt")) as f:
        parts = f.read().split("\n\n")

    for line in parts[0].strip().split("\n"):
        match = re.match(r"([0-9]+): \"([a-z]+)\"", line)
        if match is None:
            match = re.match(r"([0-9]+): (.*)", line)
            rule_id = match.group(1)
            subrules = match.group(2).split(" | ")

            p1 = [rules[a] for a in subrules[0].split(" ")]
            p2 = (
                None
                if len(subrules) == 1
                else [rules[a] for a in subrules[1].split(" ")]
            )

            rule = rules[rule_id]
            rule.p1 = p1
            rule.p2 = p2
        else:
            rule = rules[match.group(1)]
            rule.p1 = match.group(2)

    regex = rules_to_regex(rules["0"])
    print(f"regex: {regex}")
    matching_lines = 0
    for line in parts[1].strip().split("\n"):
        if re.fullmatch(regex, line):
            matching_lines += 1

    print(f"Solution: {matching_lines}")




    regex_8 = "(((a(((((ab|bb)b|(ab)a)a|(((a|b)(a|b))a|(b(a|b)|aa)b)b)b|((a(ba|bb)|b((a|b)(a|b)))a|(a(ba|aa)|b((a|b)(a|b)))b)a)b|(b((b(ba|bb)|a(ab))b|(b(b(a|b)|aa)|a(ab))a)|a(b(b((a|b)(a|b))|a(b(a|b)|aa))|a((aa)b|(ba|aa)a)))a)|b((b(b(b(aa)|a(ba))|a(b(ab|bb)|a(bb|aa)))|a(((bb)a|(b(a|b)|aa)b)b|(b(b(a|b)|aa)|a(ba|bb))a))a|(a(((ba|aa)b|(ab)a)b|((aa)b|(ab|bb)a)a)|b(b((ab|ba)a|(ba|bb)b)|a((ba|aa)a|(ba|bb)b)))b))a|((((((ba|aa)b|(ab)a)a|(b(bb|aa)|a((a|b)(a|b)))b)b|(a((ba|aa)a|(ba|a(a|b))b)|b((bb|aa)b|(ba)a))a)a|(a(((a(a|b)|bb)a|((a|b)(a|b))b)a|(a(aa)|b(ba|aa))b)|b(a(a(ba))|b(a(ba|aa)|b(b(a|b)|aa))))b)a|(((((ba|bb)b|(bb|aa)a)a|(b(ab)|a(ab|bb))b)b|(a((aa|ab)b|(ab|bb)a)|b((a|b)(a(a|b)|bb)))a)a|(a(((ba)a)b|((ba)a|(bb)b)a)|b(((bb|aa)b|(ba)a)a|(b(ab)|a(b(a|b)|aa))b))b)b)b))"
    regex_42="((a(((((ab|bb)b|(ab)a)a|(((a|b)(a|b))a|(b(a|b)|aa)b)b)b|((a(ba|bb)|b((a|b)(a|b)))a|(a(ba|aa)|b((a|b)(a|b)))b)a)b|(b((b(ba|bb)|a(ab))b|(b(b(a|b)|aa)|a(ab))a)|a(b(b((a|b)(a|b))|a(b(a|b)|aa))|a((aa)b|(ba|aa)a)))a)|b((b(b(b(aa)|a(ba))|a(b(ab|bb)|a(bb|aa)))|a(((bb)a|(b(a|b)|aa)b)b|(b(b(a|b)|aa)|a(ba|bb))a))a|(a(((ba|aa)b|(ab)a)b|((aa)b|(ab|bb)a)a)|b(b((ab|ba)a|(ba|bb)b)|a((ba|aa)a|(ba|bb)b)))b))a|((((((ba|aa)b|(ab)a)a|(b(bb|aa)|a((a|b)(a|b)))b)b|(a((ba|aa)a|(ba|a(a|b))b)|b((bb|aa)b|(ba)a))a)a|(a(((a(a|b)|bb)a|((a|b)(a|b))b)a|(a(aa)|b(ba|aa))b)|b(a(a(ba))|b(a(ba|aa)|b(b(a|b)|aa))))b)a|(((((ba|bb)b|(bb|aa)a)a|(b(ab)|a(ab|bb))b)b|(a((aa|ab)b|(ab|bb)a)|b((a|b)(a(a|b)|bb)))a)a|(a(((ba)a)b|((ba)a|(bb)b)a)|b(((bb|aa)b|(ba)a)a|(b(ab)|a(b(a|b)|aa))b))b)b)b)"
    regex_31="(b(a(b((b(a(bb)|b(ab|bb))|a((ab|ba)a|(ba|a(a|b))b))a|((a(aa|ab)|b(ab))b|(((a|b)(a|b))b|(b(a|b)|aa)a)a)b)|a((((a(a|b)|bb)b|(aa|ab)a)a|(a(ab|ba)|b(ba|bb))b)b|(((aa|ab)a|(b(a|b)|aa)b)a|(a(aa|ab)|b(ba|bb))b)a))|b(a((((aa|ab)b|(ab|bb)a)b|(b(ba|aa)|a(ab|ba))a)a|(((bb)a|(ab|ba)b)b|(b(b(a|b)|aa)|a(ba|bb))a)b)|b((a((a(a|b)|bb)(a|b))|b(b(ba|a(a|b))|a(ba)))a|(b(b(ab|bb))|a(b(b(a|b)|aa)|a(a(a|b)|bb)))b)))|a(b(b((a(b(ba|aa)|a(ba|bb)))a|(b(a(aa|ab)|b(ba|bb))|a(b(a(a|b)|bb)|a(bb|aa)))b)|a(a(((ba|aa)b|(ab)a)b|((ab)b|(aa|ab)a)a)|b(b(b(a(a|b)|bb)|a(bb|aa))|a((b(a|b)|aa)a|(ab|bb)b))))|a(b((((ab)a|((a|b)(a|b))b)b|(a(bb|aa)|b(bb))a)b|(a(a(ba))|b(b(ab|bb)))a)|a(a(((ba|bb)a|(aa|ab)b)a|(a(ab|bb)|b(bb|aa))b)|b(a(b(b(a|b)|aa)|a(ba))|b(b(a(a|b)|bb)|a(b(a|b)|aa)))))))"
    regex_11 = f"({regex_42}+{regex_31})+"
    regex_0 = f"({regex_8}+{regex_11})"

    matching_lines = 0
    for line in parts[1].strip().split("\n"):
        if re.fullmatch(f"{regex_8}({regex_42}{regex_31})", line):
            matching_lines += 1

    print(f"Solution: {matching_lines}")
    
    matching_lines = 0
    for line in parts[1].strip().split("\n"):
        if re.fullmatch(f"{regex_0}", line):
            matching_lines += 1

    print(f"Solution: {matching_lines}")



if __name__ == "__main__":
    main()
