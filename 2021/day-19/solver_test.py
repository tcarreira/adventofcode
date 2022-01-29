from solver import *
from Spacial3D import *


def test_parse_input_scanners():
    test_input = """
--- scanner 0 ---
0,0,0
0,0,1
0,0,2

--- scanner 1 ---
2,0,0
2,0,1
2,0,2
""".strip()

    assert parse_input_scanners(test_input) == {
        0: Space3D(
            [
                Point3D(0, 0, 0),
                Point3D(0, 0, 1),
                Point3D(0, 0, 2),
            ]
        ),
        1: Space3D(
            [
                Point3D(2, 0, 0),
                Point3D(2, 0, 1),
                Point3D(2, 0, 2),
            ]
        ),
    }


def test_scanner_matches_test():
    scn1 = Space3D(
        [
            Point3D(0, 0, 0),
            Point3D(1, 2, 3),
            Point3D(1, 3, 5),
            Point3D(1, 6, 9),
            Point3D(5, 1, 3),
            Point3D(5, 3, 7),
            Point3D(5, 5, 3),
            Point3D(8, 7, 6),
            Point3D(8, 7, 4),
            Point3D(8, 3, 1),
            Point3D(9, 1, 1),
            Point3D(4, 8, 3),
        ]
    )
    assert len(scn1) == 12

    rot_id = 17
    scn2 = scn1.build_all_rotations()[rot_id]
    scn1.extend([Point3D(-1, 12, 0), Point3D(17, -2, 3)])
    scn2.extend(
        [Point3D(1, 1, 1), Point3D(2, -2, 2), Point3D(2, -2, 3), Point3D(2, -2, 5)]
    )

    expected = {
        0: {1: Point3D.inverse_rotation_id(rot_id)},
        1: {0: rot_id},
    }
    matches = scanner_matches({0: scn1, 1: scn2}, 12)
    assert matches == expected

    # add one more scanner
    scn3 = scn2.build_all_rotations()[rot_id]
    scn3 = Space3D([p for i, p in enumerate(scn3) if i > 2])

    expected = {
        0: {1: Point3D.inverse_rotation_id(rot_id)},
        1: {0: rot_id, 2: Point3D.inverse_rotation_id(rot_id)},
        2: {1: rot_id},
    }
    matches = scanner_matches({0: scn1, 1: scn2, 2: scn3}, 12)
    assert matches == expected


def test_rotate_scanners():
    s0 = Space3D([Point3D(1, 2, 3)])
    s1 = s0.build_all_rotations()[15]
    s2 = s1.build_all_rotations()[19]

    matches: Dict[int, Dict[int, int]] = {
        0: {1: Point3D.inverse_rotation_id(15)},
        1: {0: 15, 2: Point3D.inverse_rotation_id(19)},
        2: {1: 19},
    }
    rotated = rotate_scanners({0: s0, 1: s1, 2: s2}, matches)

    assert rotated == {0: s0, 1: s0, 2: s0}


def test_find_displacement():
    s0 = Space3D([Point3D(i, i + 2, i + 3) for i in range(12)])
    s1 = Space3D([p + Point3D(2, 2, 2) for p in s0])
    scanners = {0: s0, 1: s1}

    # keys are irrelevant on this test
    matches = {
        0: {1: 0},
        1: {0: 0},
    }
    diffs = {s_id: scanner.build_diffs() for s_id, scanner in scanners.items()}

    displacement = find_displacement(scanners, matches, diffs, 0, 1)
    assert displacement == Point3D(2, 2, 2)


def test_move_scanners():
    s0 = Space3D([Point3D(i, i + 2, i + 3) for i in range(12)])
    s1 = Space3D([p + Point3D(2, 2, 2) for p in s0])
    s2 = Space3D([p + Point3D(3, 2, 1) for p in s1])

    # keys are irrelevant on this test
    matches = {0: {1: 0}, 1: {0: 0, 2: 0}, 2: {1: 0}}
    moved = move_scanners({0: s0, 1: s1, 2: s2}, matches)
    assert moved[0] == moved[1]


def test_from_problem_1():

    raw_input = """
--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7

--- scanner 0 ---
1,-1,1
2,-2,2
3,-3,3
2,-1,3
-5,4,-6
-8,-7,0

--- scanner 0 ---
-1,-1,-1
-2,-2,-2
-3,-3,-3
-1,-3,-2
4,6,5
-7,0,8

--- scanner 0 ---
1,1,-1
2,2,-2
3,3,-3
1,3,-2
-4,-6,5
7,0,8

--- scanner 0 ---
1,1,1
2,2,2
3,3,3
3,1,2
-6,-4,-5
0,7,-8
""".strip()
    scanners = parse_input_scanners(raw_input)
    matches = scanner_matches(scanners=scanners, overlapping=6)
    rotated_scanners = rotate_scanners(scanners=scanners, matches=matches)

    for s in rotated_scanners.values():
        assert s == rotated_scanners[0]
