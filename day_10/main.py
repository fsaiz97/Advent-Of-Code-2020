import itertools


def main():
    with open("input.txt") as file:
        adapters = [int(line) for line in file]
    
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    pairs = itertools.pairwise(adapters)

    results = {1:0, 2:0, 3:0}
    for pair in pairs:
        #print(pair)  # debug
        results[pair[1] - pair[0]] += 1

    print(results)
    print(results[1] * results[3])


if __name__ == '__main__':
    main()
