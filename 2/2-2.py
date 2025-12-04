from os import chdir, path
from textwrap import wrap
chdir(path.realpath(path.dirname(__file__)))

def repeats(id: int) -> bool:
    """Determines whether `id` (in base 10) is made up of a sequence of repeating digits"""
    return repeats_n_numbers(str(id), len(str(id)) // 2)

def repeats_n_numbers(id: str, n: int) -> bool:
    """Determines whether `id` (in base 10) is made up of a sequence of `n` repeating digits"""
    if n == 0:
        return False
    substrings = wrap(id, n) # Chop into substrings of length n
    if len(set(substrings)) == 1:
        return True
    return repeats_n_numbers(id, n - 1)

def main():
    with open('./input.txt', 'r') as f:
        id_ranges = f.read().split(',')
    ids = []
    for id_range in id_ranges:
        start, stop = id_range.split('-')
        ids.extend(range(int(start), int(stop)+1)) # +1 to include range end

    invalid_ids = [id for id in ids if repeats(id)]
    print(sum(invalid_ids))

if __name__ == "__main__":
    main()