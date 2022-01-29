#!/usr/bin/env python3

from collections import Counter, defaultdict
import itertools
import math
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, Set

from Spacial3D import Point3D, Space3D

currdir = Path(__file__).parent.absolute()
# paste the example from the problem here ↓
test_input = """
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
""".strip()

cheating_for_part_2: Dict[int, Point3D] = {}


def parse_input_scanners(scanners_raw: str) -> Dict[int, Space3D]:
    scanners: Dict[int, Space3D] = {}
    for n, scanner in enumerate(scanners_raw.split("\n\n")):
        points_list: Space3D = Space3D([])
        for line in scanner.strip().splitlines()[1:]:
            p = Point3D(*map(int, line.split(",")))
            points_list.append(p)
        scanners[n] = points_list
    return scanners


def scanner_matches(
    scanners: Dict[int, Space3D], overlapping: int
) -> Dict[int, Dict[int, int]]:
    result: Dict[int, Dict[int, int]] = {}

    scanners_with_rotations = {
        key: scan.build_all_rotations() for key, scan in scanners.items()
    }

    scans_w_rots_diffs = {
        s_id: [rot.build_diffs() for rot in scanner_rotations]
        for s_id, scanner_rotations in scanners_with_rotations.items()
    }

    # main thing
    for scan_id, scan_rots_w_diffs in sorted(scans_w_rots_diffs.items()):
        scanner_result: Dict[int, int] = {}
        scan_diffs = scan_rots_w_diffs[0]

        for tmp_scan_id, tmp_scan_rots_w_diffs in sorted(scans_w_rots_diffs.items()):
            if tmp_scan_id == scan_id:
                continue

            for rot_id, tmp_rot_diffs in enumerate(tmp_scan_rots_w_diffs):
                common_points_count = sum(
                    [len(v) // 2 for p, v in tmp_rot_diffs.items() if p in scan_diffs]
                )
                if common_points_count >= math.comb(overlapping, 2):
                    if tmp_scan_id in scanner_result:
                        print("hummm, ", tmp_scan_id, rot_id)
                    scanner_result[tmp_scan_id] = rot_id
                    # break
        result[scan_id] = scanner_result

    return result


def _rotate_scanners(
    scanners: Dict[int, Space3D],
    matches: Dict[int, Dict[int, int]],
    seen: Set[int],
    current: int,
    previous: int,
    rotations: List[int],
) -> None:
    if current in seen:
        return

    seen.add(current)
    next_rotations = rotations + [matches[current][previous]]
    for next_scanner in matches[current]:
        _rotate_scanners(
            scanners=scanners,
            matches=matches,
            seen=seen,
            current=next_scanner,
            previous=current,
            rotations=next_rotations,
        )

    # inverse rotation, from leaf to root
    for rot in next_rotations[::-1]:
        inverse_rotation_id = Point3D.inverse_rotation_id(rot)
        scanners[current] = scanners[current].rotate(inverse_rotation_id)


def rotate_scanners(
    scanners: Dict[int, Space3D], matches: Dict[int, Dict[int, int]]
) -> Dict[int, Space3D]:
    rotated_scanners = {k: s.clone() for k, s in scanners.items()}

    seen = {0}
    for next_scanner in matches[0]:
        _rotate_scanners(
            scanners=rotated_scanners,
            matches=matches,
            seen=seen,
            current=next_scanner,
            previous=0,
            rotations=[],
        )

    return rotated_scanners


def find_displacement(
    scanners: Dict[int, Space3D],
    matches: Dict[int, Dict[int, int]],
    diffs: Dict[int, Dict[Point3D, List[int]]],
    from_scan: int,
    to_scan: int,
) -> Point3D:

    # find common diffs for find the displacement
    common_diffs: Set[Point3D] = set()
    for diff in diffs[from_scan]:
        if diff in diffs[to_scan]:
            common_diffs.add(diff)

    assert len(common_diffs) > 0

    displacements: List[Point3D] = []
    for diff in common_diffs:
        idx_from_scan = diffs[from_scan][diff][0]
        idx_to_scan = diffs[to_scan][diff][0]
        displacements.append(
            scanners[to_scan][idx_to_scan] - scanners[from_scan][idx_from_scan]
        )

    displacement = Counter(displacements).most_common(1)[0][0]
    return displacement


def _move_scanners(
    scanners: Dict[int, Space3D],
    matches: Dict[int, Dict[int, int]],
    diffs: Dict[int, Dict[Point3D, List[int]]],
    seen: Set[int],
    current: int,
    previous: int,
    move_point: Point3D,
) -> None:
    if current in seen:
        return

    try:
        displacement = find_displacement(
            scanners=scanners,
            matches=matches,
            diffs=diffs,
            from_scan=previous,
            to_scan=current,
        )
    except AssertionError:
        print("Could not find displacement", current, previous)
        return
    displacement_to_origin = move_point + displacement  # why not??
    displacement_to_origin = displacement  # why??
    cheating_for_part_2[current] = -displacement

    seen.add(current)
    # do move
    scanners[current] = scanners[current].move(-displacement_to_origin)

    for next_scanner in matches[current]:
        _move_scanners(
            scanners=scanners,
            matches=matches,
            diffs=diffs,
            seen=seen,
            current=next_scanner,
            previous=current,
            move_point=displacement_to_origin,
        )


def move_scanners(
    scanners: Dict[int, Space3D], matches: Dict[int, Dict[int, int]]
) -> Dict[int, Space3D]:
    moved_scanners = {k: s.clone() for k, s in scanners.items()}
    diffs = {s_id: scanner.build_diffs() for s_id, scanner in scanners.items()}

    seen = {0}
    for next_scanner in matches[0]:
        _move_scanners(
            scanners=moved_scanners,
            matches=matches,
            diffs=diffs,
            seen=seen,
            current=next_scanner,
            previous=0,
            move_point=Point3D(0, 0, 0),
        )

    return moved_scanners


def part1(scanners: Dict[int, Space3D], overlapping: int = 12) -> Any:

    matches = scanner_matches(scanners=scanners, overlapping=overlapping)
    rotated_scanners = rotate_scanners(scanners=scanners, matches=matches)
    moved_scanners = move_scanners(scanners=rotated_scanners, matches=matches)

    all_points: DefaultDict[Point3D, int] = defaultdict(int)
    for s in moved_scanners.values():
        for p in s:
            all_points[p] += 1

    solution = len(all_points)
    return solution


def part2(scanners: Dict[int, Space3D], overlapping: int = 12) -> Any:

    scanners_positions = cheating_for_part_2
    scanners_positions[0] = Point3D(0, 0, 0)

    max_dist = 0
    for s1, s2 in itertools.combinations(scanners_positions.values(), 2):
        d = s1 - s2
        manh_dist = abs(d.x) + abs(d.y) + abs(d.z)
        if manh_dist > max_dist:
            max_dist = manh_dist
    solution = max_dist

    return solution


def main() -> None:
    raw_input = open(currdir.joinpath("input.txt")).read()
    # raw_input = test_input  # testing with the example - comment for real input
    scanners = parse_input_scanners(raw_input)

    print("Solution to Part 1:")
    print(part1(scanners))

    print("Solution to Part 2:")
    print(part2(scanners))


if __name__ == "__main__":
    main()
