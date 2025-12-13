from os import chdir, path

chdir(path.realpath(path.dirname(__file__)))

NR_TICKS = 100

state = 50
zero_counter = 0
with open('./input.txt', 'r') as f:
    for input_line in f.readlines():
        previous_state = state
        go_left = input_line[0] == 'L'
        distance = int(input_line[1:])
        if go_left: distance = -distance
        
        state += distance
        zero_counter += abs(int(state / NR_TICKS))
        if state <= 0 and previous_state > 0:
            zero_counter += 1
        state = state % NR_TICKS

print(zero_counter)