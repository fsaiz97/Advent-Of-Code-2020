import re
from collections import deque
from dataclasses import dataclass


TARGET_COLOUR = "shiny gold"


@dataclass
class Node:
    """Creates a node object with an arbitrary number of children and depth first search.
    """
    colour: str


@dataclass
class Relation:
    """Creates a directed link between a parent Node and a child Node, along with a weight.
    """
    parent: Node
    child: Node
    weight: int


@dataclass
class Tree:
    """Represents a tree data structure with a list of Node objects and a set of Relations between nodes in the node list
    """
    nodes: list[Node]
    relations: list[Relation]


def read_input():
    """Read and parse the input."""
    with open("input.txt") as file:
        regex = re.compile("(?P<colour>[a-z]+ [a-z]+) bags contain (?P<contents>[^.]+)")

        input_matches = [regex.match(line) for line in file]
        print(f"{len(input_matches) = }")

    return input_matches


def parse_bag_contents(line_match):
    """Reads the bag contents."""
    regex = re.compile("(?P<quantity>\d+) (?P<colour>[a-z]+ [a-z]+)")
 
    if line_match.group('contents') == "no other bags":
        return []
    else:
        contents = [string.strip() for string in line_match.group('contents').split(',')]
        #print("contents: ", contents) # debug
        content_matches = [regex.match(content) for content in contents]
        return content_matches


def create_tree(input_matches):
    """Creates a tree of bags and their contents."""
    nodes= []
    relations = []

    for match in input_matches:
        if match != None:
            bag = Node(match.group('colour'))
            #print(f"{bag = }") # debug
            nodes.append(bag)

            content_matches = parse_bag_contents(match)
            for content_match in content_matches:
                child = Node(content_match.group('colour'))
                relations.append(Relation(bag, child, int(content_match.group('quantity'))))

    print(f"{nodes = }\n{relations = }")

    return Tree(nodes, relations)


def find_holding_bags(bag, relations, holding_bags_set):
    print(f"{bag = }")
    filtered = [relation for relation in relations if relation.child.colour == bag.colour]
    print("Parents:", [relation.parent.colour for relation in filtered]) # debug
    for relation in filtered:
        holding_bags_set = find_holding_bags(relation.parent, relations, holding_bags_set)

    if bag.colour != TARGET_COLOUR:
        holding_bags_set.add(bag.colour)
    
    return holding_bags_set


def main():
    """Takes a set of packing instructions for bags and returns all bags which
    can hold a certain bag 'gold' directly or indirectly.
    Directly means the target bag is inside the containing bag, indrectly 
    means the target bag is inside one or more bags which are inside the
    containing bag.
    """

    target_bag: Node = Node(TARGET_COLOUR)

    input_matches = read_input()
    tree = create_tree(input_matches)
    holding_bags_set = find_holding_bags(target_bag, tree.relations, set())

    print("Answer:", len(holding_bags_set))


if __name__ == '__main__':
    main()
