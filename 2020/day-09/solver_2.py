#!/usr/bin/env python3

import collections
import os

from solver_1 import MyFIFO, main as solver1

curdir = os.path.dirname(os.path.realpath(__file__))


def main():
    invalid_element = solver1()

    with open(curdir + "/input.txt") as f:
        fifo = MyFIFO(invalid_element)  # infinite

        for line in f.readlines():
            number = int(line.strip())
            fifo.append(number)

            # Keep appending until "invalid" element
            if number != invalid_element:
                continue

            for start in range(0, len(fifo)):
                sum = 0
                for end in range(start, len(fifo)):
                    if sum == invalid_element:
                        items_list = [fifo.fifo[i] for i in range(start, end)]
                        minim = min(items_list)
                        maxim = max(items_list)
                        print(f"min: {minim}, Max: {maxim}, items: {items_list}")
                        print(f"Sum: {minim+maxim}")
                        return
                    elif sum > invalid_element:
                        break

                    sum += fifo.fifo[end]


if __name__ == "__main__":
    main()
