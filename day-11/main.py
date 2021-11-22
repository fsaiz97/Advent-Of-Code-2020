import argparse
frok dataclasses import dataclass


parser = argparse.ArgumentParser(description="Takes in the input to day 11")
parser.add_argument('input', help="Stores the input file name")
args = parser.parse_args()


@dataclass
class Point:
    x: int
    y: int


def parse_input():
    with open(args.input) as file:
        area = [list(line.strip()) for line in file]

    return area


def run(area):
    position = Point(0, 0)

    future = area

    while True:
        for i, line in enumerate(area):
            for j, tile in enumerate(line):
                if tile == '.':
                    future
                    continue
                else:
                    if check_rules(tile, area):
                        
                    else:
                        pass


def main():
    area = parse_input()

    width = len(area[0])
    height = len(area)

    run(area)


if __name__ == '__main__':
    main()
