from os import chdir, path

def is_fresh(ingredient_id: int, fresh_ranges: list[tuple[int, int]]) -> bool:
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def main():
    chdir(path.realpath(path.dirname(__file__)))
    fresh_ranges = []
    with open('./input.txt', 'r') as f:
        while (line := f.readline()) != "\n": # Read lines until finding an empty one
            start, stop = line.split("-")
            fresh_ranges.append((int(start), int(stop)))
        count = 0
        for ingredient_id in f.readlines():
            count += is_fresh(int(ingredient_id), fresh_ranges)
    print(count)

if __name__ == "__main__":
    main()