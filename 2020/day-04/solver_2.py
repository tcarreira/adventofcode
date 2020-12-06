#!/usr/bin/env python3

import os
import re

curdir = os.path.dirname(os.path.realpath(__file__))


class Passport:
    MANDATORY_FIELDS = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    }

    def __init__(self):
        self.byr = ""
        self.iyr = ""
        self.eyr = ""
        self.hgt = ""
        self.hcl = ""
        self.ecl = ""
        self.pid = ""
        # self.cid = ""

    def verify(self):
        for field in self.MANDATORY_FIELDS:
            if not self.verify_field(field):
                return False
        return True

    def verify_field(self, field):
        if field == "byr":
            return self.verify_byr()
        if field == "iyr":
            return self.verify_iyr()
        if field == "eyr":
            return self.verify_eyr()
        if field == "hgt":
            return self.verify_hgt()
        if field == "hcl":
            return self.verify_hcl()
        if field == "ecl":
            return self.verify_ecl()
        if field == "pid":
            return self.verify_pid()

    def verify_byr(self):
        return self._verify_number(
            self.byr,
            min=1920,
            max=2002,
        )

    def verify_iyr(self):
        return self._verify_number(
            self.iyr,
            min=2010,
            max=2020,
        )

    def verify_eyr(self):
        return self._verify_number(
            self.eyr,
            min=2020,
            max=2030,
        )

    def verify_hgt(self):
        match = re.search("^([0-9]*)(cm|in)$", self.hgt)
        if match and len(match.groups()) == 2:
            if match.group(2) == "cm":
                return self._verify_number(
                    match.group(1),
                    min=150,
                    max=193,
                )
            elif match.group(2) == "in":
                return self._verify_number(
                    match.group(1),
                    min=59,
                    max=76,
                )

    def verify_hcl(self):
        match = re.search("^#[0-9a-f]{6}$", self.hcl)
        return match is not None

    def verify_ecl(self):
        match = re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", self.ecl)
        return match is not None

    def verify_pid(self):
        match = re.search("^[0-9]{9}$", self.pid)
        return match is not None

    def _verify_number(self, v, min, max):
        try:
            i = int(v)
            if min <= i <= max:
                return True
        except Exception:
            pass


def main():
    with open(curdir + "/input.txt") as f:
        document = Passport()
        valid = 0

        for line in f.readlines():
            if line.strip() == "":
                if document.verify():
                    valid += 1
                document = Passport()
            else:
                for field_value in line.strip().split(" "):
                    field, value = field_value.split(":")[0:2]
                    setattr(document, field, value)

        # check if last line was not blank, but a valid passport
        if document.verify():
            valid += 1

        print(f"Valid passports: {valid}")


if __name__ == "__main__":
    main()
