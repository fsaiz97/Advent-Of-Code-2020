import itertools
import argparse
from trees import Node, Relation, Tree

parser = argparse.ArgumentParser(description="Takes the input file as an argument")
parser.add_argument('input', help="Stores the input text file.")
args = parser.parse_args()


def old_slow_count_paths(current, adapters, count=0):
    for next_ in range(current + 1, current + 4):
        if next_ not in adapters:
            continue

        if next_ == adapters[-1]:
            count += 1
            break
        else:
            count = old_slow_count_paths(next_, adapters, count)

        print(f"For {current}, {count =}")
    return count


def find_fixed_runs(tree):
    runs = []
    curr_run = []
    capture_flg = True  # starts capturing from 0
    active_nodes = [tree.nodes[0]]

    while True:
        # print(f"{active_nodes = }\n")  # debug

        if len(active_nodes) == 0:
            runs.append(curr_run)
            print("last run:", curr_run)
            break
        elif len(active_nodes) == 1:
            capture_flg = True
            curr_run.append(active_nodes[0].data)
        elif len(active_nodes) > 1 and capture_flg:
            print(f"{curr_run = }")  # debug
            runs.append(curr_run.copy())
            curr_run.clear()
            capture_flg = False

        for child in tree.find_children(active_nodes[0]):
            if child not in active_nodes:
                active_nodes.append(child)
        active_nodes.pop(0)

    return runs


def fast_count_paths(adapters, runs):
    print(f"{runs = }")
    count = 1
    for index, run in enumerate(runs):
        if index != len(runs) - 1:
            print(f"{run = }")
            count *= slow_count_paths(run[-1], adapters, end=runs[index + 1][0])
            print(f"{run[-1] = }, {runs[index+1][0] = }")
            print(f"{count = }")

    return count


def slow_count_paths(current, adapters, count=0, end=None):
    for next_ in range(current + 1, current + 4):
        if next_ not in adapters:
            continue

        if next_ == end:
            count += 1
            break
        else:
            count = slow_count_paths(next_, adapters, count, end)

    print(f"For {current}, {count =}")  # debug
    return count


def create_tree(adapters):
    nodes = [Node(adapter) for adapter in adapters]

    relations = []
    for node in nodes:
        children = [num for num in range(node.data + 1, node.data + 4) if num in adapters]
        for child in children:
            relations.append(Relation(node, Node(child)))

    return Tree(nodes, relations)


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

    tree = create_tree(adapters)
    runs = find_fixed_runs(tree)

    count = fast_count_paths(adapters, runs)

    # count = slow_count_paths(adapters[0], adapters)

    print("part 2 answer:", count)


if __name__ == '__main__':
    main()
