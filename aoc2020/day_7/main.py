import re
import argparse
from .common import trees


# creates an argument parser to take cli arguments
parser = argparse.ArgumentParser(description="Solves Advent of Code 2020 day 7.")
parser.add_argument('input', help="the input file to read from")
parser.add_argument('target', help="the bag that the puzzle is solved for")
args = parser.parse_args()


def read_input():
    """Read the input and split each line into a bag and its contents."""
    with open(args.input) as file:
        temp = [line.split('contain') for line in file]
        lines = [[line[0].strip(), line[1].strip()] for line in temp]
        # print(lines[:10])  # debug
        # print(f"{len(lines) = }")  # debug

    return lines


def parse_bag_contents(raw_contents, regex):
    """Parses the bag contents to extract the quantity and colour of each contained bag."""

    if raw_contents == "no other bags.":
        return []
    else:
        contents = [string.strip() for string in raw_contents.split(',')]
        # print("contents: ", contents) # debug
        content_matches = [regex.match(content) for content in contents]
        return content_matches


def create_tree(lines):
    """Creates a tree of bags and their contents."""
    nodes = []
    relations = []
    regex = re.compile(r"(?P<quantity>\d+)?(\s+)?(?P<colour>[a-z]+ [a-z]+)")

    for line in lines:
        match = regex.match(line[0])
        if not match:
            raise Exception
        # print("Groups:", match.groups())  # debug
        bag = Node(match.group('colour'))
        # print(f"{bag = }") # debug
        nodes.append(bag)

        content_matches = parse_bag_contents(line[1], regex)

        for content_match in content_matches:
            child = Node(content_match.group('colour'))
            relations.append(Relation(bag, child, int(content_match.group('quantity'))))

    # print(f"{nodes = }\n{relations = }")

    return Tree(nodes, relations)


def find_holding_bags(bag, relations, holding_bags_set=set()):
    """Answers part 1 by counting all bags which can hold the target bag.
    Uses recursion to explore all ancestors of the target bag in a depth first search"""
    # print(f"{bag = }")  # debug
    filtered = [relation for relation in relations if relation.child == bag]
    # print("Parents:", [relation.parent.colour for relation in filtered])  # debug
    for relation in filtered:
        holding_bags_set = find_holding_bags(relation.parent, relations, holding_bags_set)

    if bag.colour != args.target:
        # prevents the first level of recursion from adding the target bag
        # to the set of bags which can hold it
        holding_bags_set.add(bag.colour)

    return holding_bags_set


def count_child_nodes(bag, relations, multiplier=1, count=0):
    """Counts the total number of bags held by the target bag"""
    for relation in relations:
        if relation.parent == bag:
            count = count_child_nodes(relation.child, relations, multiplier * relation.weight, count)

    if bag.colour != args.target:
        # prevents the target bag from being counted in the bags it can hold
        count += multiplier

    return count


def main():
    """Takes a set of packing instructions for bags and returns all bags which
    can hold a certain bag 'gold' directly or indirectly.
    Directly means the target bag is inside the containing bag, indirectly
    means the target bag is inside one or more bags which are inside the
    containing bag.
    """
    target_bag: Node = Node(args.target)
    lines = read_input()
    tree = create_tree(lines)
    if target_bag not in tree.nodes:
        raise LookupError("Bag not found.")
    holding_bags_set = find_holding_bags(target_bag, tree.relations)
    count = count_child_nodes(target_bag, tree.relations)

    print("Part 1 Answer:", len(holding_bags_set))
    print(f"Part 2 Answer:", count)


if __name__ == '__main__':
    main()
