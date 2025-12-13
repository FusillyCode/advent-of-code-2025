from os import chdir, path
import numpy as np
from numpy.typing import NDArray
from itertools import combinations
from math import prod

class Circuit:
    def __init__(self, box: Junction_Box) -> None:
        self.boxes = set([box])
    
    def __repr__(self) -> str:
        return f"C({len(self.boxes)})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Circuit):
            return NotImplemented
        return self.boxes == value.boxes
    
    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Circuit): return NotImplemented
        return len(self.boxes) < len(value.boxes)
    
    def __hash__(self) -> int:
        l = [ord(c) for c in str(self.boxes)]
        return sum(l)
    
    def __len__(self) -> int:
        return len(self.boxes)

class Junction_Box:
    def __init__(self, coords: NDArray) -> None:
        self.coords = coords
        self.circuit = Circuit(self)
    
    def __repr__(self) -> str:
        return str(self.coords)
    
    def connect(self, other: Junction_Box) -> None:
        """Move all boxes in `self`'s circuit to `other`'s circuit"""
        if self.circuit == other.circuit: return
        other.circuit.boxes.update(self.circuit.boxes)
        for box in self.circuit.boxes:
            box.circuit = other.circuit
    
class Edge:
    """Edges aren't real connection between junction boxes, they just keep track of pairwise distances"""
    def __init__(self, a: Junction_Box, b: Junction_Box) -> None:
        self.boxes = set((a, b))
        self.distance = np.linalg.norm(a.coords - b.coords)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Edge): return NotImplemented
        return self.distance == value.distance
    
    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Edge): return NotImplemented
        return bool(self.distance < value.distance)
    
    def __repr__(self) -> str:
        return f"E({self.boxes})"

def main():
    chdir(path.realpath(path.dirname(__file__)))
    
    N_CONNECTIONS = 1000
    with open('./input.txt', 'r') as f:
        box_coords = np.array([[int(x) for x in line.strip().split(",")] for line in f])
    boxes = [Junction_Box(coords) for coords in box_coords]
    edges = sorted([Edge(a, b) for a, b in combinations(boxes, 2)])
    circuits = []
    for edge in edges[:N_CONNECTIONS]:
        box_a, box_b = edge.boxes
        box_a.connect(box_b)
    circuits = sorted(set([box.circuit for box in boxes]), reverse=True)
    print(prod([len(c) for c in circuits[:3]]))

if __name__ == "__main__":
    main()