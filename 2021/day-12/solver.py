#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip()

test_input2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip()

test_input3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".strip()


# part 1
def walk_path(connections, start="start", end="end"):
    if start == end:
        return 1
    if start not in connections:
        return 0

    next_points = connections[start]
    connections = {a: b for a, b in connections.items() if a != start or a.isupper()}
    paths = 0
    for point in next_points:
        paths += walk_path(connections, point)
    return paths


# part 2
def walk_unique_path(connections, unique_paths, path="start", start="start", end="end"):
    if start == end:
        unique_paths.add(path)
        return 1
    if start not in connections:
        return 0

    next_points = connections[start]
    connections = {a: b for a, b in connections.items() if a != start or a.isupper()}
    paths = 0
    for point in next_points:
        new_path = f"{path}-{point}" if point[0] != "_" else f"{path}-{point[1:-1]}"
        paths += walk_unique_path(connections, unique_paths, new_path, point)
    return paths


def part1(p_input):
    connections = defaultdict(list)
    for a, b in p_input:
        connections[a].append(b)
        connections[b].append(a)

    solution = walk_path(connections=connections)
    return solution


def part2(p_input):
    connections, small_caves = defaultdict(list), set()
    for a, b in p_input:
        connections[a].append(b)
        connections[b].append(a)

        if a == "start" or a == "end" or b == "start" or b == "end":
            continue
        if a.islower():
            small_caves.add(a)
        if b.islower():
            small_caves.add(b)

    unique_paths = set()
    walk_unique_path(connections, unique_paths)  # init unique_paths with base case
    for small_cave in small_caves:
        new_connections = {a: b for a, b in connections.items()}
        # duplicate one small cave
        new_connections[f"_{small_cave}_"] = [x for x in new_connections[small_cave]]
        for c, v in new_connections.items():
            if small_cave in v:
                new_connections[c].append(f"_{small_cave}_")

        walk_unique_path(new_connections, unique_paths)

    return len(unique_paths)


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    connections = [line.split("-") for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(connections))

    print("Solution to Part 2:")
    print(part2(connections))


if __name__ == "__main__":
    main()
