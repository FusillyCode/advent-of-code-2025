from os import chdir, path
from numpy import argmax
chdir(path.realpath(path.dirname(__file__)))

total_joltage = 0
with open('./input.txt', 'r') as f:
    for bank_string in f.readlines():
        bank = list(bank_string.strip('\n'))
        # Ignore the last battery
        first_battery = argmax(bank[:-1])
        # Ignore the already picked battery; account for the index offset from trimming the start of the list
        second_battery = argmax(bank[first_battery+1:]) + first_battery+1
        joltage = bank[first_battery] + bank[second_battery] # Concatenate the characters
        total_joltage += int(joltage)
print(total_joltage)