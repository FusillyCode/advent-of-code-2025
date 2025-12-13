from os import chdir, path

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        manifold = [list(line[:-1]) for line in f] # Trim newline characters

    splits = 0
    for row in range(1, len(manifold)):
        for col in range(len(manifold[0])):
            char_above = manifold[row-1][col]
            if char_above != "S" and char_above != "|":
                continue
            this_char = manifold[row][col]
            if this_char == "^":
                splits += 1
                manifold[row][col-1] = "|"
                manifold[row][col+1] = "|"
            else:
                manifold[row][col] = "|"

    print(splits)

if __name__ == "__main__":
    main()