from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    """Creates a node object with an arbitrary number of children and depth first search."""
    data: Any


@dataclass
class Relation:
    """Creates a directed link between a parent Node and a child Node, along with a weight.
    """
    parent: Node
    child: Node
    weight: int = 1


@dataclass
class Tree:
    """Represents a tree data structure with a list of Node objects
    and a set of Relations between nodes in the node list
    """
    nodes: list[Node]
    relations: list[Relation]

    def find_parents(self, target):
        return [relation.parent for relation in self.relations if relation.child == target]

    def find_children(self, target):
            return [relation.child for relation in self.relations if relation.parent == target]


