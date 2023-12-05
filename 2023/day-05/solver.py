#!/usr/bin/env python3

from pathlib import Path

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip()


def seed_to_location(maps, seed):
    prev = seed
    for name, submaps in maps.items():
        for mapping in submaps:
            dest, source, rang = mapping
            if prev in range(source, source + rang):
                prev = dest + (prev - source)
                break
    return prev


# 0:30:08
def part1(p_input):
    inparts = p_input.strip().split("\n\n")
    seeds = [int(x) for x in inparts[0].split(": ")[1].split(" ")]

    maps = {}
    for mmap in inparts[1:]:
        maps[mmap.split(" ")[0]] = [
            list(map(int, [x.strip() for x in l.split(" ")]))
            for l in mmap.split("\n")[1:]
        ]

    solution = float("+inf")
    for seed in seeds:
        solution = min(solution, seed_to_location(maps, seed))

    return int(solution)


def transform(submaps, ranges):
    out_ranges = []
    for maprange in ranges:
        while len(maprange) > 0:
            for mapping in submaps:
                dest, source, rang = mapping
                start = maprange[0]
                if start in range(source, source + rang):
                    dest_start = dest + (start - source)
                    if len(maprange) <= source + rang - start:
                        out_ranges.append(range(dest_start, dest_start + len(maprange)))
                        maprange = []
                    else:
                        out_ranges.append(
                            range(dest_start, dest_start + (rang - (start - source)))
                        )
                        maprange = range(source + rang, maprange[-1] + 1)
                    break
            else:
                try:
                    next_min_source = min(
                        [x[1] for x in submaps if x[1] >= maprange[0]]
                    )
                    out_ranges.append(range(maprange[0], next_min_source))
                    maprange = range(next_min_source, maprange[-1] + 1)
                except:
                    out_ranges.append(maprange)
                    maprange = []

    return out_ranges


def relax_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    out_ranges = []
    pending = ranges.pop(0)
    while len(ranges) > 0:
        curr = ranges.pop(0)
        if pending[-1] + 1 >= curr[0]:
            pending = range(pending[0], curr[-1] + 1)
        else:
            out_ranges.append(pending)
            pending = curr
    out_ranges.append(pending)
    return out_ranges


# 2:34:34
def part2(p_input):
    inparts = p_input.strip().split("\n\n")
    seeds = [int(x) for x in inparts[0].split(": ")[1].split(" ")]
    ranges = [
        range(seeds[2 * n], (seeds[2 * n] + seeds[2 * n + 1]))
        for n in range(len(seeds) // 2)
    ]

    maps = {}
    for mmap in inparts[1:]:
        maps[mmap.split(" ")[0]] = [
            list(map(int, [x.strip() for x in l.split(" ")]))
            for l in mmap.split("\n")[1:]
        ]

    for name, submaps in maps.items():
        # print(name, ranges)
        print(name, "seeds:", sum([len(x) for x in ranges]))
        [x[0] for x in ranges]  # assertR
        ranges = transform(submaps, ranges)
        ranges = relax_ranges(ranges)

    solution = min([r[0] for r in ranges if r[0] != 0])
    return solution
    # 34361884 too high
    # 34361884


def main():
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input

    # simple treat input
    p_input = raw_input
    # p_input = [line for line in raw_input.splitlines()]
    # p_input = [int(line) for line in raw_input.splitlines()]

    print("Solution to Part 1:")
    print(part1(p_input))

    print("Solution to Part 2:")
    print(part2(p_input))


if __name__ == "__main__":
    main()
