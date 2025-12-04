from os import chdir, path
from numpy import argmax

def combine_n_batteries(bank: list[str], n_batteries: int = 12) -> int:
    """Compute the joltage of combining `n_batteries` batteries in `bank`"""
    joltage = ""
    picked_index = -1
    for picks_left in range(n_batteries-1, -1, -1):
        # `picks_left` is how many batteries we still have to pick AFTER this one
        # Ignore all batteries to the left of the one we picked last; leave enough batteries to pick `picks_left` more
        sub_bank = bank[picked_index+1 : -picks_left]
        if picks_left == 0: # :-0 makes an empty list
            sub_bank = bank[picked_index+1:]
        # Account for the index offset that results from trimming the start of the list
        picked_index = argmax(sub_bank) + picked_index+1
        joltage += bank[picked_index] # String concatenation
    return int(joltage)

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        bank_strings = f.readlines()
    joltages = [combine_n_batteries(list(bank.strip('\n'))) for bank in bank_strings]
    print(sum(joltages))

if __name__ == "__main__":
    main()