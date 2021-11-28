import argparse
from copy import copy, deepcopy
import itertools
import cProfile
import pstats
from math import prod
from typing import Tuple


def add_tuples(a: Tuple, b: Tuple):
    return tuple(sum(elem) for elem in zip(a, b))


def scale_tuple(a: Tuple, m: int):
    return tuple(elem * m for elem in a)


def get_directions(dimension):
    deltas = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == 0 and j == 0)]
 
    counter = itertools.count
    directions = []
    for delta in deltas:
        direction = [scale_tuple(delta, i) for i in range(1, dimension+1)]
        directions.append(direction)

    return directions


def cli_parse():
    """setup parser to get input file name."""
    parser = argparse.ArgumentParser(description="Takes in the input to day 11")
    parser.add_argument('input', help="Stores the input file name")
    args = parser.parse_args()

    return args


def parse_input():
    """Reads input into a grid"""
    with open(args.input) as file:
        room = [list(line.strip()) for line in file]

    return room


def in_range(point, width, height):
    return (0 <= point[0] < width and 0 <= point[1] < height)


def check_surroundings(position, room, directions, width, height, distance):
    count = 0

    for direction in directions:
        for index, offset in enumerate(direction, start=1):
            # print(offset)
            if distance is not None and index > distance:
                break

            point = add_tuples(position, offset)
            # print(point)  # debug
            if not in_range(point, width, height):
                break

            tile = room[point[1]][point[0]] 
            if tile != '.':
                if tile == '#':
                    count += 1
                break

    return count


def update(position, current, directions, width, height):
    """Return the tile's next state based on the rules"""
    tile = current[position[1]][position[0]]
    occupied = check_surroundings(position, current, directions, width, height, distance = None)

    if tile == 'L':
        if occupied == 0:
            return '#'
        else:
            return None
    elif tile == '#':
        if occupied >= 5:
            return 'L'
        else:
            return None

def profile_function(room):
    width = len(room[0])
    height = len(room)

    directions = get_directions(max(width, height))

    while True:
        current = deepcopy(room)

        for y, line in enumerate(current):
            for x, tile in enumerate(line):
                if tile == '.':
                    continue

                position = (x, y)
                char = update(position, current, directions, width, height)
                if char is not None:
                    room[y][x] = char

        # print(room)  # debug

        if room == current:
            break

    return room


def main():
    # read input into 2d array
    room = parse_input()
    #print(room)  # debug

    #update loop
    with cProfile.Profile() as profile:
        room = profile_function(room)
        ps = pstats.Stats(profile)
        ps.sort_stats('tottime')
        ps.print_stats()

    occupied = len([tile for line in room for tile in line if tile == '#'])
    print("Answer =", occupied)


if __name__ == '__main__':
    args = cli_parse()

    # main code
    main()

