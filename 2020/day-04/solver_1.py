#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))
MANDATORY_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]


def check_passport(document):
    for field in MANDATORY_FIELDS:
        if field not in document:
            return False
    return True


def main():
    with open(curdir + "/input.txt") as f:
        document = {}
        valid = 0

        for line in f.readlines():
            if line.strip() == "":
                if check_passport(document):
                    valid += 1
                document = {}
            else:
                for field_value in line.split(" "):
                    field = field_value.split(":")[0]
                    document[field] = True

        # check if last line was not blank, but a valid passport
        if check_passport(document):
            valid += 1

        print(f"Valid passports: {valid}")


if __name__ == "__main__":
    main()