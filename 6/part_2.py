from os import chdir, path
from numpy import array, sum, prod
from typing import Callable

def get_operation(column: list[str]) -> Callable|None: 
    if column[-1] == "+":
        return sum
    if column[-1] == "*":
        return prod
    return None

def get_number(column: list[str]) -> int|None:
    number_string = ""
    for s in column[:-1]:
        number_string += s
    return int(number_string)

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        worksheet = array([list(line.strip("\n")) for line in f]).T
    numbers = []
    operation = sum
    accumulator = 0
    for column in worksheet:
        if (column == " ").all():
            accumulator += operation(numbers)
            numbers = []
            continue
            
        new_operation = get_operation(column)
        if new_operation: operation = new_operation
        number = get_number(column)
        if number: numbers.append(number)

    accumulator += operation(numbers) # Last op would be missed since there is no empty column at the end
    print(accumulator)

if __name__ == "__main__":
    main()