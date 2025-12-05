from os import chdir, path

def remove_accessible_rolls(grid: list[list[str]]) -> tuple[list[list[str]], int]:
    n_rows = len(grid)
    n_cols = len(grid[0])
    new_grid = grid.copy()
    rolls_removed = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if is_accessible(grid, row, col):
                new_grid[row][col] = "." # Remove roll
                rolls_removed += 1
    return new_grid, rolls_removed

def is_accessible(grid: list[list[str]], row: int, col: int) -> bool:
    if grid[row][col] != "@": return False
    n_rows = len(grid)
    n_cols = len(grid[0])
    n_neighbors = 0
    for neighbor_row in     range(max(row-1, 0), min(row+2, n_rows)):
        for neighbor_col in range(max(col-1, 0), min(col+2, n_cols)):
            if neighbor_row == row and neighbor_col == col: continue
            n_neighbors += grid[neighbor_row][neighbor_col] == "@"
    return n_neighbors < 4

def main():
    chdir(path.realpath(path.dirname(__file__)))
    grid = []
    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            grid.append(list(line.strip("\n")))
    total_rolls_removed = 0
    while True:
        grid, rolls_removed = remove_accessible_rolls(grid)
        if rolls_removed == 0:
            break
        total_rolls_removed += rolls_removed
    print(total_rolls_removed)
    

if __name__ == "__main__":
    main()