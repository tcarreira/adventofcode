from Spacial3D import *
from itertools import combinations


def test_Point3D():
    p = Point3D(1, 2, 3)
    assert p.x == 1
    assert p.y == 2
    assert p.z == 3


def test_Point3D_sub():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(-1, -2, -3)
    assert p2 - p1 == Point3D(-2, -4, -6)
    assert p1 - p2 == Point3D(2, 4, 6)


def test_Point3D_diff():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(-1, -2, -3)
    assert p1.diff(p2) == p2.diff(p1)


def test_Point3D_diff__same_xy():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(1, 2, -3)
    assert p1.diff(p2) == p2.diff(p1)


def test_Point3D_all_rotations():
    p1 = Point3D(1, 2, 3)

    all_rotations = p1.all_rotations()
    # all rotations are different
    for r1, r2 in zip(all_rotations, all_rotations[1:]):
        assert r1 != r2


def test_Point3D_inverse_rotations():
    p1 = Point3D(1, 2, 3)

    all_rotations = p1.all_rotations()
    # all rotations are different
    for r, rotated in enumerate(all_rotations):
        assert p1 == rotated.inverse_rotation(r)


def test_Point3D_clone():
    p1 = Point3D(1, 2, 3)
    p2 = p1.clone()

    p1.x = 9
    assert p1.x != p2.x


def test_Point3D_negative():
    p1 = Point3D(1, 2, 3)
    assert -p1 == Point3D(-1, -2, -3)


###
# Space3D
###
def test_Space3D():
    p1 = Point3D(0, 0, 0)
    p2 = Point3D(1, 2, 3)
    space = Space3D([p1, p2])
    assert space == [p1, p2]


def test_Space3D_empty():
    space = Space3D([])
    assert space == []


def test_Space3D_append():
    p1 = Point3D(0, 0, 0)
    p2 = Point3D(1, 2, 3)
    space = Space3D([p1])
    space.append(p2)
    assert space == [p1, p2]


def test_Space3D_getitem():
    p1 = Point3D(0, 0, 0)
    p2 = Point3D(1, 2, 3)
    space = Space3D([p1, p2])
    assert space[0] == p1
    assert space[1] == p2


def test_Space3D_build_all_rotations():
    p1 = Point3D(0, 0, 0)
    p2 = Point3D(1, 2, 3)
    space = Space3D([p1, p2])

    all_rotations = space.build_all_rotations()
    assert len(all_rotations) == 24
    assert all_rotations[0] == space

    # all rotations are different
    for r1, r2 in combinations(all_rotations, 2):
        assert r1 != r2


def test_Space3D_move():
    s1 = Space3D([Point3D(0, 0, 0), Point3D(2, 2, 2)])
    s2 = s1.move(Point3D(1, 2, 3))

    expected = Space3D([Point3D(1, 2, 3), Point3D(3, 4, 5)])
    assert expected == s2


def test_Space3D_clone():
    s1 = Space3D([Point3D(1, 0, 0)])
    s2 = s1.clone()
    s2.append(Point3D(1, 2, 3))

    s1[0].x = 9
    assert s1 != s2
    assert len(s1) == 1
    assert len(s2) == 2
    assert s1[0].x == s2[0].x  # no deep_clone


def test_Space3D_deep_clone():
    s1 = Space3D([Point3D(1, 0, 0)])
    s2 = s1.deep_clone()

    s1[0].x = 9
    assert s1 != s2
    assert s1[0].x != s2[0].x


def test_Space3D_rotate():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(5, 5, 9)
    s1 = Space3D([p1, p2])

    rotated = s1.rotate(17)

    assert rotated == Space3D(
        [
            p1.rotate(17),
            p2.rotate(17),
        ]
    )
