from dataclasses import dataclass


@dataclass
class Node:
    """Creates a node object with an arbitrary number of children and depth first search."""
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
    """Represents a tree data structure with a list of Node objects
    and a set of Relations between nodes in the node list
    """
    nodes: list[Node]
    relations: list[Relation]


