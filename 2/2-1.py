from os import chdir, path
chdir(path.realpath(path.dirname(__file__)))


def repeats_twice(id_int: int) -> bool:
    """Determines whether `id_int` (in base 10) is made up of a sequence of digits repeated twice"""
    id = str(id_int)
    if len(id) % 2 != 0: # Odd sequences can't be equally split
        return False
    middle = len(id) // 2
    return id[:middle] == id[middle:]

with open('./input.txt', 'r') as f:
    id_ranges = f.read().split(',')
ids = []
for id_range in id_ranges:
    start, stop = id_range.split('-')
    ids.extend(range(int(start), int(stop)))

invalid_ids = [id for id in ids if repeats_twice(id)]
print(sum(invalid_ids))