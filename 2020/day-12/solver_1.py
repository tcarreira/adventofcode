#!/usr/bin/env python3

import os

curdir = os.path.dirname(os.path.realpath(__file__))


#   N
# W - E
#   S
class Ship:
    def __init__(self):
        self.lon = 0  # x
        self.lat = 0  # y
        self.direction = 0  # E=0º, N=90º...

    def get_direction(self):
        return {0: "E", 90: "N", 180: "W", 270: "S"}[self.direction % 360]

    def turn(self, direction, degrees):
        self.direction += {
            "R": -degrees,
            "L": degrees,
        }[direction]

    def north(self, direction, distance):
        self.lat += distance

    def south(self, direction, distance):
        self.lat -= distance

    def east(self, direction, distance):
        self.lon += distance

    def west(self, direction, distance):
        self.lon -= distance

    def forward(self, direction, distance):
        self.move(self.get_direction(), distance)

    def move(self, direction, distance):
        {
            "R": self.turn,
            "L": self.turn,
            "N": self.north,
            "E": self.east,
            "S": self.south,
            "W": self.west,
            "F": self.forward,
        }[direction](direction, distance)


def main():
    ship = Ship()
    with open(curdir + "/input.txt") as f:
        for line in f.readlines():
            ship.move(line[0], int(line.strip()[1:]))

    print(f"Position: x={ship.lon} y={ship.lat}")
    print(f"Manhattan Distance: {abs(ship.lon)+abs(ship.lat)}")


if __name__ == "__main__":
    main()
