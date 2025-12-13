from os import chdir, path
chdir(path.realpath(path.dirname(__file__)))

state = 50
zero_counter = 0
with open('./input.txt', 'r') as f:
    for input_line in f.readlines():
        direction = input_line[0]
        distance = int(input_line[1:])
        distance = distance if direction == 'R' else -distance
        state = (state + distance) % 100
        if state == 0:
            zero_counter += 1

print(zero_counter)