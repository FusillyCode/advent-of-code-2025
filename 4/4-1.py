from os import chdir, path

def is_accessible(grid: list, row: int, col: int) -> bool:
    if grid[row][col] != "@": return False
    n_rows = len(grid)
    n_cols = len(grid[0]) - 1 # Ignore the \n characters
    n_neighbors = 0
    for neighbor_row in     range(max(row-1, 0), min(row+2, n_rows)):
        for neighbor_col in range(max(col-1, 0), min(col+2, n_cols)):
            if neighbor_row == row and neighbor_col == col: continue
            n_neighbors += grid[neighbor_row][neighbor_col] == "@"
    return n_neighbors < 4

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        grid = f.readlines()
    n_rows = len(grid)
    n_cols = len(grid[0]) - 1 # Ignore the \n characters
    n_accessible_rolls = 0
    for row in range(n_rows):
        for col in range(n_cols):
            n_accessible_rolls += is_accessible(grid, row, col)
    print(n_accessible_rolls)

if __name__ == "__main__":
    main()