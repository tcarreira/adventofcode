#!/usr/bin/env python3

from math import ceil, sqrt
from pathlib import Path

curdir = Path(__file__).parent.absolute()

# baby-step giant-step algorithm
# kudos to https://github.com/mebeim
def bsgs(base, n, p):
    m = ceil(sqrt(p))
    table = {pow(base, i, p): i for i in range(m)}

    # base^(-m) mod p == base^(m*(p-2)) assuming p is prime
    inv = pow(base, (p - 2) * m, p)
    res = None

    for i in range(m):
        y = (n * pow(inv, i, p)) % p
        if y in table:
            res = i * m + table[y]
            break

    return res


def main():
    rem = 20201227
    with open(curdir.joinpath("input.txt")) as f:
        public_keys = [int(x) for x in f.read().splitlines()]

    loop_size = bsgs(7, public_keys[0], rem)
    key = pow(public_keys[1], loop_size, rem)

    print("Encryption key:", key)


if __name__ == "__main__":
    main()
