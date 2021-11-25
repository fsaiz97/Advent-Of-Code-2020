import argparse
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def parse_input():
    with open(args.input) as file:
        waiting_area = [list(line.strip()) for line in file]

    return waiting_area


def in_range(point, x_bound, y_bound):
    return (0 <= point.x <= x_bound and 0 <= point.y <= y_bound)


def fetch_adjacent(point, waiting_area):
    width = len(waiting_area[0])
    height = len(waiting_area)

    adjacent_points = [Point(point.x + i, point.y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == 0 and j == 0)]
    adjacent = [waiting_area[adjacent_point.x][adjacent_point.y] for adjacent_point in adjacent_points if in_range(adjacent_point, width-1, height-1)]

    return adjacent


def update_tile(point, waiting_area):
    """Return the tile's next state based on the rules"""
    tile = waiting_area[point.x][point.y]

    adjacent = fetch_adjacent(point, waiting_area)
    occupied = adjacent.count('#')
    # print(occupied)  # debug

    if tile == 'L':
        if occupied == 0:
            return '#'
        else:
            return tile
    elif tile == '#':
        if occupied >= 4:
            return 'L'
        else:
            return tile


def run(waiting_area):

    next_state = waiting_area

    while True:
        for j, line in enumerate(waiting_area):
            for i, tile in enumerate(line):
                if tile == '.':
                    continue
                else:
                    next_state[i][j] = update_tile(Point(i,j), waiting_area)

        if next_state == waiting_area:
            break

        waiting_area = next_state

    print("Part 1 answer =", len([tile for line in waiting_area for tile in line if tile == '#']))


def main():
    waiting_area = parse_input()

    run(waiting_area)


if __name__ == '__main__':
    # setup parser to get input file name
    parser = argparse.ArgumentParser(description="Takes in the input to day 11")
    parser.add_argument('input', help="Stores the input file name")
    args = parser.parse_args()

    # main code
    main()
