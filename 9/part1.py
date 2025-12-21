from os import chdir, path
from itertools import combinations

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        grid = [tuple(map(int, line.strip().split(","))) for line in f]
    area = 0
    for corners in combinations(grid, 2):
        width =     abs(corners[0][0] - corners[1][0]) + 1
        length =    abs(corners[0][1] - corners[1][1]) + 1
        area = max(area, width*length)
    print(area)
if __name__ == "__main__":
    main()