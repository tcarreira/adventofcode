#!/usr/bin/env python3

from pathlib import Path

curdir = Path(__file__).parent.absolute()


class Node:
    cache = {}

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        Node.cache[value] = self

    def pop(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        return self

    def insert(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def __hash__(self):
        return self.value

    def __str__(self):
        return self.value.__str__()

    def __repr__(self):
        return "[%s]" % self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, node):
        self.len += 1
        if self.head is None:
            self.head = node
        elif self.head.next is None:
            node.next = node.prev = self.head
            self.head.next = self.head.prev = node
        else:
            self.head.prev.insert(node)

    def __len__(self):
        return self.len

    def __str__(self):
        output = [str(self.head)]

        curr = self.head.next
        while curr != self.head:
            output.append(str(curr))
            curr = curr.next

        return " -> ".join(output)

    def __repr__(self):
        return str(self)


def simulate(linked, moves, idx=0, picked=3):
    total = len(linked)

    current = linked.head
    for k in range(moves):
        if k % 10000 == 0:
            print(f"\r{k*100//moves} %",end="")

        moving = []
        for _ in range(picked):
            moving.append(current.next.pop())

        destination = (current.value -2) % total + 1
        while Node.cache[destination] in moving:
            destination = (destination - 2) % total + 1
        
        for m in reversed(moving):
            Node.cache[destination].insert(m)
        
        current = current.next
    print("")

def main():
    with open(curdir.joinpath("input.txt")) as f:
        numbers = [int(x) for x in f.read().strip()]

    linked = LinkedList()
    for n in range(1000000):
        if n < len(numbers):
            linked.insert(Node(numbers[n]))
        else:
            linked.insert(Node(n+1))
     

    simulate(linked, 10000000)
    result = [ Node.cache[1].next.value, Node.cache[1].next.next.value ]

    print(result)
    print(f"Solution: {result[0]*result[1]}")


if __name__ == "__main__":
    main()
