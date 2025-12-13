from os import chdir, path
import numpy as np
from itertools import combinations
from part_1 import Junction_Box, Edge
    
def all_in_one_circuit(boxes: list[Junction_Box]) -> bool:
    circ = boxes[0].circuit
    for box in boxes[1:]:
        if box.circuit != circ:
            return False
    return True

def main():
    chdir(path.realpath(path.dirname(__file__)))
    
    with open('./input.txt', 'r') as f:
        box_coords = np.array([[int(x) for x in line.strip().split(",")] for line in f])
    boxes = [Junction_Box(coords) for coords in box_coords]
    edges = sorted([Edge(a, b) for a, b in combinations(boxes, 2)])
    box_a, box_b = None, None
    for edge in edges:
        box_a, box_b = edge.boxes
        box_a.connect(box_b)
        if all_in_one_circuit(boxes): break
 
    if box_a is not None and box_b is not None: print(box_a.coords[0] * box_b.coords[0])

if __name__ == "__main__":
    main()