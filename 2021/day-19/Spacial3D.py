from collections import defaultdict
from typing import DefaultDict, Dict, Iterable, List, SupportsIndex, Union, overload


class Point3D:
    @staticmethod
    def normalize_diff(p1: "Point3D", p2: "Point3D") -> "Point3D":
        "normalize the difference between 2 points, so diff(a,b) == diff(b,a)"
        if p1.x < p2.x:
            return p2 - p1
        if p1.x == p2.x and p1.y < p2.y:
            return p2 - p1
        if p1.x == p2.x and p1.y == p2.y and p1.z < p2.z:
            return p2 - p1
        return p1 - p2

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def clone(self) -> "Point3D":
        return Point3D(self.x, self.y, self.z)

    def all_rotations(self) -> List["Point3D"]:
        x, y, z = self.x, self.y, self.z
        return [
            # ---
            Point3D(x, y, z),
            Point3D(y, -x, z),
            Point3D(-x, -y, z),
            Point3D(-y, x, z),
            # ---
            Point3D(x, -z, y),
            Point3D(-z, -x, y),
            Point3D(-x, z, y),
            Point3D(z, x, y),
            # ---
            Point3D(x, -y, -z),
            Point3D(-y, -x, -z),
            Point3D(-x, y, -z),
            Point3D(y, x, -z),
            # ---
            Point3D(x, z, -y),
            Point3D(z, -x, -y),
            Point3D(-x, -z, -y),
            Point3D(-z, x, -y),
            # ---
            Point3D(-z, y, x),
            Point3D(y, z, x),
            Point3D(z, -y, x),
            Point3D(-y, -z, x),
            # --- ---
            Point3D(z, y, -x),
            Point3D(y, -z, -x),
            Point3D(-z, -y, -x),
            Point3D(-y, z, -x),
        ]

    @staticmethod
    def inverse_rotation_id(id: int) -> int:
        return {
            0: 0,
            1: 3,
            2: 2,
            3: 1,
            4: 12,
            5: 23,
            6: 6,
            7: 17,
            8: 8,
            9: 9,
            10: 10,
            11: 11,
            12: 4,
            13: 19,
            14: 14,
            15: 21,
            16: 20,
            17: 7,
            18: 18,
            19: 13,
            20: 16,
            21: 15,
            22: 22,
            23: 5,
        }[id]

    def inverse_rotation(self, rotation_id: int) -> "Point3D":
        return self.all_rotations()[self.inverse_rotation_id(rotation_id)]
        # x, y, z = self.x, self.y, self.z
        # return [
        #     # ---
        #     Point3D(x, y, z), #0  0
        #     Point3D(-y, x, z), #3
        #     Point3D(-x, -y, z), #2
        #     Point3D(y, -x, z), #1
        #     # ---
        #     Point3D(x, z, -y), #12  4
        #     Point3D(-y, z, -x),#23
        #     Point3D(-x, z, y), #6
        #     Point3D(y, z, x), #17
        #     # ---
        #     Point3D(x, -y, -z), #8  8
        #     Point3D(-y, -x, -z), #9
        #     Point3D(-x, y, -z), #10
        #     Point3D(y, x, -z), #11
        #     # ---
        #     Point3D(x, -z, y), #4  12
        #     Point3D(-y, -z, x), #19
        #     Point3D(-x, -z, -y), #14
        #     Point3D(y, -z, -x),#21
        #     # ---
        #     Point3D(z, y, -x),#20 16
        #     Point3D(z, x, y), #7
        #     Point3D(z, -y, x), #18
        #     Point3D(z, -x, -y), #13
        #     # --- ---
        #     Point3D(-z, y, x),#16 20
        #     Point3D(-z, x, -y),#15
        #     Point3D(-z, -y, -x),#22
        #     Point3D(-z, -x, y), #5
        # ]

    def rotate(self, idx: int) -> "Point3D":
        return self.all_rotations()[idx]

    def diff(self, p2: "Point3D") -> "Point3D":
        "normalize the difference between 2 points, so a.diff(b) == b.diff(b)"
        if not isinstance(p2, type(self)):
            return NotImplemented

        if self.x < p2.x:
            return p2 - self
        if self.x == p2.x and self.y < p2.y:
            return p2 - self
        if self.x == p2.x and self.y == p2.y and self.z < p2.z:
            return p2 - self
        return self - p2

    def __str__(self) -> str:
        return f"P({self.x},{self.y},{self.z})"

    def __repr__(self) -> str:
        return "r" + str(self)

    def __sub__(self, __o: object) -> "Point3D":
        if not isinstance(__o, type(self)):
            return NotImplemented
        return Point3D(self.x - __o.x, self.y - __o.y, self.z - __o.z)

    def __add__(self, __o: object) -> "Point3D":
        if not isinstance(__o, type(self)):
            return NotImplemented
        return Point3D(self.x + __o.x, self.y + __o.y, self.z + __o.z)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, type(self)):
            return NotImplemented
        return self.x == __o.x and self.y == __o.y and self.z == __o.z

    def __neg__(self) -> "Point3D":
        return Point3D(-self.x, -self.y, -self.z)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


# Space3D = List[Point3D]
class Space3D(List[Point3D]):
    @overload
    def __setitem__(self, index: SupportsIndex, value: Point3D) -> None:
        ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[Point3D]) -> None:
        ...

    def __setitem__(
        self,
        index: Union[SupportsIndex, slice],
        value: Union[Point3D, Iterable[Point3D]],
    ) -> None:
        # Administrative stuff deleted
        if isinstance(index, slice) and isinstance(value, Iterable):
            super().__setitem__(index, value)
        elif isinstance(index, int) and isinstance(value, Point3D):
            super().__setitem__(index, value)
        else:
            raise TypeError(f"{index}/{value} Invalid index/value type.")

    def build_all_rotations(self) -> List["Space3D"]:
        all_rotations: List["Space3D"] = [Space3D([]) for _ in self[0].all_rotations()]

        for p in self:
            for r, rotated_point in enumerate(p.all_rotations()):
                all_rotations[r].append(rotated_point)

        return all_rotations

    def build_diffs(self) -> Dict[Point3D, List[int]]:
        result: DefaultDict[Point3D, List[int]] = defaultdict(list)
        for i, p1 in enumerate(self):
            for j, p2 in enumerate(self[i + 1 :], start=i + 1):
                result[p1.diff(p2)].extend([i, j])
        return result

    def rotate(self, rotation_id: int) -> "Space3D":
        return Space3D([p.rotate(rotation_id) for p in self])

    def clone(self) -> "Space3D":
        return Space3D([p for p in self])

    def deep_clone(self) -> "Space3D":
        return Space3D([p.clone() for p in self])

    def move(self, to: Point3D) -> "Space3D":
        return Space3D([p + to for p in self])
