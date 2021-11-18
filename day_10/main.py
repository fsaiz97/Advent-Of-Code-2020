import itertools
import argparse


parser = argparse.ArgumentParser(description="Takes the input file as an argument")
parser.add_argument('input', help="Stores the input text file.")
args = parser.parse_args()


def count_paths(current, adapters, count=0):
    for next_ in range(current+1, current+4):
        if next_ not in adapters:
            continue

        if next_ == adapters[-1]:
            count += 1
            break
        else:
            count = count_paths(next_, adapters, count)

        print(f"For {current}, {count =}")
    return count


def main():
    with open(args.input) as file:
        adapters = [int(line) for line in file]

    # adds socket and device joltages
    adapters.append(0)
    adapters.append(max(adapters) + 3)

    # order adapters and collates consecutive pairs
    adapters.sort()
    pairs = itertools.pairwise(adapters)

    results = {1: 0, 2: 0, 3: 0}
    for pair in pairs:
        # print(pair)  # debug
        results[pair[1] - pair[0]] += 1

    print(results)
    print("part 1 answer:", results[1] * results[3])

    count = count_paths(adapters[0], adapters)

    print("part 2 answer:", count)


if __name__ == '__main__':
    main()
