import argparse
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    N = 0
    E = 90
    S = 180
    W = 270


def get_vector(direction, distance):
    print(Direction(direction))

class Ship:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def update(self, opcode, operand):
        if opcode == 'N':
            self.point.y += operand
        elif opcode == 'S':
            self.point.y -= operand
        elif opcode == 'E':
            self.point.x += operand
        elif opcode == 'W':
            self.point.x -= operand
        elif opcode == 'S':
            self.point.y -= operand
        elif opcode == 'L':
            pass



def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    return parser.parse_args()


def parse_input():
    instructions = []
    with open(args.input) as file:
        for line in file:
            instructions.append((line[0], int(line[1:])))
    # print(instructions)  # debug

    return instructions


def main():
    get_vector('E', 10)
    exit()
    ship = Ship(0+0j, 'E')

    instructions = parse_input()

    for instruction in instructions:
        ship.update(instruction[0], instruction[1])


if __name__ == '__main__':
    args = parse_cli()

    main()
