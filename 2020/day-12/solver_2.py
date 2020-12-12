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

        self.wp_lon = 10  # x===E
        self.wp_lat = 1  # y===N

    def turn(self, direction, degrees):
        degrees = degrees if direction == "L" else -degrees

        self.wp_lon, self.wp_lat = {
            0: (self.wp_lon, self.wp_lat),
            90: (-self.wp_lat, self.wp_lon),
            180: (-self.wp_lon, -self.wp_lat),
            270: (self.wp_lat, -self.wp_lon),
        }[degrees % 360]

    def north(self, direction, distance):
        self.wp_lat += distance

    def south(self, direction, distance):
        self.wp_lat -= distance

    def east(self, direction, distance):
        self.wp_lon += distance

    def west(self, direction, distance):
        self.wp_lon -= distance

    def forward(self, direction, distance):
        self.lon += distance * self.wp_lon
        self.lat += distance * self.wp_lat

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
