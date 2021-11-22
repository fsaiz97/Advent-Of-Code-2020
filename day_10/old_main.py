import itertools
import argparse


parser = argparse.ArgumentParser(description="Takes the input file as an argument")
parser.add_argument('input', help="Stores the input text file.")
args = parser.parse_args()


def old_slow_count_paths(current, adapters, count=0):
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


def find_fixed_runs(adapters):
    runs = []
    curr_run = []
    capture_flg = True  # starts capturing from 0
    for index, adapter in enumerate(adapters):
        if capture_flg:
            curr_run.append(adapter)

            # if there are multiple choices for the next adapter
            if (index >= len(adapters) - 2) or (adapters[index+2] in range(adapter+1, adapter+4)):
                print(index)
                print(adapters[index+2])
                runs.append(curr_run)
                print(f"{curr_run = }")
                curr_run.clear()
                capture_flg == False
        else:
            # if the previous adapter in sequence doesnt have multiple adapters it can connect to next
            prev = adapter[index-1]
            if (index == len(adapters) - 1) or (adapter[index+1] not in range(prev+1, prev+4)):
                capture_flg = True
                curr_run.append(adapter)

    return runs


def fast_count_paths(adapters, runs):
    count = 1
    for index, run in enumerate(runs):
        if index != len(runs) - 1:
            print(f"{run = }")
            count *= slow_count_paths(run[-1], adapters, runs[index+1][0])
            print(f"{run[-1] = }")

    return count


def slow_count_paths(current, adapters, count=0, end=None):
    for next_ in range(current+1, current+4):
        if next_ not in adapters:
            continue

        if next_ == end :
            count += 1
            break
        else:
            count = count_paths(next_, adapters, count)

        #  print(f"For {current}, {count =}")  # debug
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

    runs = find_fixed_runs(adapters)

    count = fast_count_paths(adapters, runs)

    # count = slow_count_paths(adapters[0], adapters)

    print("part 2 answer:", count)


if __name__ == '__main__':
    main()
