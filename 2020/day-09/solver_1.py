#!/usr/bin/env python3

import collections
import os

curdir = os.path.dirname(os.path.realpath(__file__))


class MyFIFO:
    def __init__(self, size):
        self.size = size
        self.fifo = collections.deque()
        self.indexed = {}

    def __len__(self):
        return len(self.fifo)

    def _index_element(self, element):
        if element in self.indexed:
            self.indexed[element] += 1
        else:
            self.indexed[element] = 1

    def append(self, element):
        if len(self.fifo) >= self.size:
            popped = self.pop()
            self.indexed[popped] -= 1

        self._index_element(element)
        return self.fifo.append(element)  # append to right

    def pop(self):
        return self.fifo.popleft()

    def search(self, element):
        return element in self.indexed and self.indexed[element] > 0

    def is_sum_of_two(self, element):
        for e in self.fifo:
            if element == e:
                continue
            if element - e in self.fifo:
                return True
        return False


def check_number(fifo, element):
    if len(fifo) >= fifo.size: # the first N elements are the preamble
        if not fifo.is_sum_of_two(element):
            print(f"This is the first 'wrong' element: {element}")
            return False
    fifo.append(element)
    return True


def main(preamble=25):
    with open(curdir + "/input.txt") as f:
        fifo = MyFIFO(preamble)

        for line in f.readlines():
            number = int(line.strip())
            if not check_number(fifo, number):
                return number


if __name__ == "__main__":
    main()
