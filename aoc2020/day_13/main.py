import argparse
import itertools
import math


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    return parser.parse_args()


def parse_input():
    with open(args.input) as file:
        timestamp = int(file.readline().strip())
        buses = [int(bus) if bus != 'x' else bus for bus in file.readline().strip().split(',')]

    return timestamp, buses


def find_earliest_bus(timestamp, buses):
    for time in itertools.count(timestamp):
        for bus in buses:
            if time % bus == 0:
                return time, bus


def slow_part_2(buses, step):
    for time in itertools.count(0, step=step):
        flag = True
        # print(f"{time = }")  # debug
        for index, bus in enumerate(buses):
            if bus == 'x':
                continue
            if (time + index) % bus != 0:
                flag = False
                break
        if flag:
            print("Part 2 =", time)
            break


def crt(integers, modulo):
    """Solves the simultaenous modulus equations using the chinese remainder theorem"""
    N = math.prod(integers)


def main():
    timestamp, buses = parse_input()
    active = [bus for bus in buses if bus != 'x']

    time, bus = find_earliest_bus(timestamp, active)

    answer = bus * (time - timestamp)

    print("Part 1 =", answer)

    print(f"{active[0] = }")

    step = active[0]        

    
if __name__ == '__main__':
    args = parse_cli()
    main()
