#!/usr/bin/env python3

import re
from collections import defaultdict
from pathlib import Path

curdir = Path(__file__).parent.absolute()



def main():
    with open(curdir.joinpath("input.txt")) as f:
        tile_coords = f.read().splitlines()
    
    black_tiles = set()

    for tile in tile_coords:
        i=0
        position = (0,0,0)
        while i < len(tile.strip()):
            if i < len(tile.strip())-1 and tile[i:i+2] == "se":
                position = (
                    position[0]+1,
                    position[1],
                    position[2]-1,
                )
                i+=2
            elif i < len(tile.strip())-1 and tile[i:i+2] == "sw":
                position = (
                    position[0],
                    position[1]-1,
                    position[2]-1,
                )
                i+=2
            elif i < len(tile.strip())-1 and tile[i:i+2] == "ne":
                position = (
                    position[0],
                    position[1]+1,
                    position[2]+1,
                )
                i+=2
            elif i < len(tile.strip())-1 and tile[i:i+2] == "nw":
                position = (
                    position[0]-1,
                    position[1],
                    position[2]+1,
                )
                i+=2
            elif tile[i] == "e":
                position = (
                    position[0]+1,
                    position[1]+1,
                    position[2],
                )
                i+=1
            elif tile[i] == "w":
                position = (
                    position[0]-1,
                    position[1]-1,
                    position[2],
                )
                i+=1
            else:
                print(f"Fuuuuuu. i={i}, line={tile}")
                return
        
        print(position)
        if position in black_tiles:
            black_tiles.remove(position)
        else:
            black_tiles.add(position)


    print("Solution: ", len(black_tiles))

if __name__ == "__main__":
    main()


# se se nw ne ne ne w se e sw w sw swwnenewsewsw
# ne e e ne se nw nw w sw ne ne w nw w se w ne nw se sw e sw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew

