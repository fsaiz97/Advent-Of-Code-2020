import argparse
from dataclasses import dataclass
from copy import copy, deepcopy


@dataclass
class Point:
    x: int
    y: int

    def add(self, point):
        self.x += point.x
        self.y += point.y

    def addw(self, point):
        return Point(self.x + point.x, self.y + point.y)



def cli_parse():
    """setup parser to get input file name."""
    parser = argparse.ArgumentParser(description="Takes in the input to day 11")
    parser.add_argument('input', help="Stores the input file name")
    args = parser.parse_args()

    return args


def parse_input():
    """Reads input into a grid"""
    with open(args.input) as file:
        waiting_area = [list(line.strip()) for line in file]

    return waiting_area


def in_range(point, width, height):
    return (0 <= point.x < width and 0 <= point.y < height)


def fetch_adjacent(point, waiting_area):
    width = len(waiting_area[0])
    height = len(waiting_area)

    adjacent_points = [Point(point.x + i, point.y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == 0 and j == 0)]
    adjacent = [waiting_area[adjacent_point.y][adjacent_point.x] for adjacent_point in adjacent_points if in_range(adjacent_point, width, height)]

    return adjacent


def in_sight(point, waiting_area):
    width = len(waiting_area[0])
    height = len(waiting_area)

    adjacent_points = [Point(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == 0 and j == 0)]
    count = 0
    for adj_point in adjacent_points:
        orig = copy(adj_point)
        print(orig)
        coord = point.addw(adj_point)
        while in_range(coord, width, height):
            if waiting_area[coord.y][coord.x] == '#':
                count += 1
                break

            adj_point.add(orig)
            if adj_point == Point(0,0):
                exit("bu")

    return count


def update_tile(point, waiting_area, mode):
    """Return the tile's next state based on the rules"""
    tile = waiting_area[point.y][point.x]
    if mode == 1:
        adjacent = fetch_adjacent(point, waiting_area)
        occupied = adjacent.count('#')
    elif mode == 2:
        occupied = in_sight(point, waiting_area)
    # print(occupied)  # debug

    if tile == 'L':
        if occupied == 0:
            return '#'
        else:
            return tile
    elif tile == '#':
        if occupied >= 3+mode:
            return 'L'
        else:
            return tile


def run(waiting_area, part):

    next_state = deepcopy(waiting_area)

    while True:
        for j, line in enumerate(waiting_area):
            for i, tile in enumerate(line):
                if tile == '.':
                    continue
                else:
                    next_state[j][i] = update_tile(Point(i,j), waiting_area, mode=part)

        # print(next_state)  # debug

        if next_state == waiting_area:
            break
        else:
            waiting_area = deepcopy(next_state)

    print(f"{part } answer =", len([tile for line in waiting_area for tile in line if tile == '#']))


def main():
    waiting_area = parse_input()

    run(waiting_area, part=1)

    run(waiting_area, part=2)


if __name__ == '__main__':
    args = cli_parse()

    # main code
    main()

