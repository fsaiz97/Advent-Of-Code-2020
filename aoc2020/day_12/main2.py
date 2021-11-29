import argparse
from dataclasses import dataclass
from enum import Enum
import math
import cmath


CIRCLE = 360


class Ordinal(Enum):
    N = 0
    E = 90
    S = 180
    W = 270


def get_vector(distance, direction):
    angle = Ordinal[direction].value  # angle in degrees
    z = cmath.rect(distance, math.radians(angle))

    return round_complex(z)


def round_complex(z):
    return complex(round(z.real), round(z.imag))


class Ship:
    # Positions are represented with complex numbers where the real part is north/south and the imaginary part is east/west.
    # Direction is an compass direction enumerating the corresponsing angle.
    def __init__(self, position, direction, waypoint):
        self.position = position
        self.direction = direction
        self.waypoint = waypoint

    def update(self, opcode, operand):
        if opcode in ('N', 'E', 'S', 'W'):
            self.waypoint += get_vector(operand, opcode)
        elif opcode in ('L', 'R'):
            angle = math.radians(operand)
            print(f"{self.direction = } {angle = }")
            if opcode == 'L':
                self.waypoint *= cmath.rect(1, -1 * angle)
            elif opcode == 'R':
                self.waypoint *= cmath.rect(1, angle)
            self.waypoint = round_complex(self.waypoint)
        elif opcode == 'F':
            self.position += self.waypoint * operand
  

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


def manhatten(z):
    return abs(z.real) + abs(z.imag) 

def main():
    ship = Ship(0+0j, 'E', 1+10j)

    instructions = parse_input()

    for instruction in instructions:
        print(ship.position, ship.waypoint)
        ship.update(instruction[0], instruction[1])

    print(ship.position)
    print("Final position =", int(manhatten(ship.position)))


if __name__ == '__main__':
    args = parse_cli()

    main()
