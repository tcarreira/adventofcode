import sys
from pathlib import Path

import regex

curdir = Path(__file__).parent.absolute()

# Solution from https://github.com/viliampucik/adventofcode
# shame on me


def solve(rules, messages):
    def expand(value):
        if not value.isdigit():
            return value
        return "(?:" + "".join(map(expand, rules[value].split())) + ")"

    r = regex.compile(expand("0"))
    return sum(r.fullmatch(m) is not None for m in messages)


def main():

    with open(curdir.joinpath("input.txt")) as f:
        raw_rules, messages = f.read().split("\n\n")

    messages = messages.splitlines()
    rules = dict(
        raw_rule.replace('"', "").split(": ", 1) for raw_rule in raw_rules.splitlines()
    )

    print(solve(rules, messages))
    rules["8"] = "42 +"  # repeat pattern
    rules["11"] = "(?P<R> 42 (?&R)? 31 )"  # recursive pattern
    print(solve(rules, messages))


if __name__ == "__main__":
    main()
