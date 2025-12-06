from os import chdir, path
from numpy import array, int32, str_
from numpy.typing import NDArray

def parse_int(s: str) -> int|str:
    try:    return int(s)
    except: return s

def evaluate(numbers: NDArray[int32], operator: str_) -> int32:
    if operator == "+":
        return numbers.sum()
    if operator == "*":
        return numbers.prod()
    raise ValueError(f"Last element \"{operator}\" is not a recognized operator")

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        numbers_arrays = array([[parse_int(x) for x in line.split()] for line in f][:-1], dtype=int32).T
        f.seek(0)
        operators = array([line.split() for line in f][-1], dtype=str_).T
    results = [evaluate(numbers, operator) for numbers, operator in zip(numbers_arrays, operators)]
    print(sum(results))

if __name__ == "__main__":
    main()